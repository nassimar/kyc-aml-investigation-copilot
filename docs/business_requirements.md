# Business Requirements — KYC / AML Investigation Copilot

## 1. Client Context

Client: Atlas Bank (fictional financial institution)

Industry: Banking and Financial Services

Department: Compliance / Financial Crime Prevention

## 2. Business Problem

KYC analysts spend significant time reviewing customer documents, verifying information completeness, consulting internal procedures, and preparing investigation reports.

Manual processing can create delays, inconsistencies, and operational inefficiencies.

## 3. Project Objective

Develop an AI-powered copilot that assists compliance analysts in reviewing customer files, retrieving relevant compliance procedures, and preparing traceable investigation reports.

## 4. Target Users

- KYC Analysts
- Compliance Officers
- Financial Crime Investigation Teams

## 5. MVP Scope

- Load synthetic customer files
- Extract and structure customer information
- Identify missing information using defined business rules
- Retrieve relevant internal policies using RAG
- Generate preliminary reports with source references
- Require human validation

## 6. Success Metrics

- Document extraction accuracy
- Missing-information detection precision and recall
- Retrieval relevance
- Citation accuracy
- Average processing time per dossier
- Percentage of reports requiring human correction

## 7. Constraints

- Synthetic customer data only
- No autonomous account approval or rejection
- Human-in-the-loop validation
- Traceability of retrieved information
- No secrets or confidential information in GitHub

## 8. Planned Technology Stack

Python, LangChain, LangGraph, ChromaDB, FastAPI, Streamlit, Docker, MLflow, GitHub Actions.