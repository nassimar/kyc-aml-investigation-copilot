import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BASE_DIR / "data" / "synthetic" / "customers.json"

REQUIRED_DOCUMENTS = {"registration", "identity", "address"}


def validate_customer(customer):
    issues = []

    # Check required information
    if not customer.get("registration_number"):
        issues.append("Missing registration number")

    if not customer.get("beneficial_owner"):
        issues.append("Missing beneficial owner")

    # Check required documents
    provided_documents = set(customer.get("documents", []))
    missing_documents = REQUIRED_DOCUMENTS - provided_documents

    for document in sorted(missing_documents):
        issues.append(f"Missing document: {document}")

    # Check consistency between declared countries
    declared_country = customer.get("declared_country")

    if declared_country and declared_country != customer.get("country"):
        issues.append("Country information mismatch")

    return {
        "customer_id": customer["customer_id"],
        "status": "REVIEW_REQUIRED" if issues else "NO_ISSUES_FOUND",
        "issues": issues,
    }


def main():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        customers = json.load(file)

    for customer in customers:
        result = validate_customer(customer)

        print(f"\nCustomer: {result['customer_id']}")
        print(f"Status: {result['status']}")

        for issue in result["issues"]:
            print(f"  - {issue}")


if __name__ == "__main__":
    main()
