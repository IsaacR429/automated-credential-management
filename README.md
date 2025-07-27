#  Automated Credential Management for Onboarding

This project automates the secure creation and registration of credentials (e.g., client IDs, secrets, tokens) during FinTech client onboarding workflows. It was developed as part of my master's thesis on AI-powered workflow automation.

##  Purpose

Manual credential generation is error-prone and slow. This project automates:
- Generating strong client secrets
- Registering them with environment-specific storage (e.g., AWS Secrets Manager, Vault)
- Providing structured logs or alerts for completion

##  Technologies Used

- Python
- `secrets`, `uuid`, `hashlib` – for secure key/token generation
- `boto3` or `hvac` – for storing credentials in secret managers
- YAML – for configuration files
- Logging

##  Features

-  Generates strong random client secrets
-  Supports integration with secure stores (Vault / AWS Secrets Manager)
-  Structured logging
-  Can be extended to CLI or API trigger
