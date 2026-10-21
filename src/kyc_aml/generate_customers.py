import json
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Where we will save our synthetic data
OUTPUT_DIR = BASE_DIR / "data" / "synthetic"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

customers = [
    {
        "customer_id": "KYC-001",
        "company_name": "Atlas Trading SAS",
        "country": "France",
        "registration_number": "SYNTH-001",
        "beneficial_owner": "Alice Martin",
        "documents": ["registration", "identity", "address"]
    },
    {
        "customer_id": "KYC-002",
        "company_name": "Nova Consulting SARL",
        "country": "France",
        "registration_number": "SYNTH-002",
        "beneficial_owner": "Karim Benali",
        "documents": ["registration", "identity"]
    },
    {
        "customer_id": "KYC-003",
        "company_name": "Orion Logistics SAS",
        "country": "Belgium",
        "registration_number": "SYNTH-003",
        "beneficial_owner": None,
        "documents": ["registration", "identity", "address"]
    },
    {
        "customer_id": "KYC-004",
        "company_name": "Blue Horizon Ltd",
        "country": "Ireland",
        "registration_number": "SYNTH-004",
        "beneficial_owner": "Emma Wilson",
        "documents": ["registration", "identity", "address"],
        "declared_country": "France"
    },
    {
        "customer_id": "KYC-005",
        "company_name": "Global Ventures SAS",
        "country": "France",
        "registration_number": None,
        "beneficial_owner": None,
        "documents": ["identity"]
    }
]

output_file = OUTPUT_DIR / "customers.json"

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(customers, f, indent=4, ensure_ascii=False)

print(f"Created {len(customers)} synthetic customer records.")
print(f"Saved to: {output_file}")
