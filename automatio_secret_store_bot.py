import boto3
import json
import time
from botocore.exceptions import ClientError

# === Load your secrets from secrets_test.json ===
with open('bot/secrets_test.json', 'r') as f:
    secrets_test = json.load(f)

# === Start your session ===
session = boto3.Session(profile_name='xxx')
secrets_client = session.client('secretsmanager')

# === Start timing ===
start_time = time.time()

for secret_name, secret_value in secrets_test.items():
    try:
        # Try to get the secret value
        response = secrets_client.get_secret_value(SecretId=secret_name)
        current_value = json.loads(response['SecretString'])
        
        if current_value != secret_value:
            print(f"[INFO] Secret '{secret_name}' exists but needs update.")
            secrets_client.put_secret_value(
                SecretId=secret_name,
                SecretString=json.dumps(secret_value)
            )
            print(f"[UPDATED] Secret '{secret_name}' updated.")
        else:
            print(f"[OK] Secret '{secret_name}' exists and is up-to-date.")
            
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print(f"[INFO] Secret '{secret_name}' not found. Creating it...")
            secrets_client.create_secret(
                Name=secret_name,
                SecretString=json.dumps(secret_value)
            )
            print(f"[CREATED] Secret '{secret_name}' created successfully.")
        else:
            print(f"[ERROR] Something went wrong with '{secret_name}': {e}")

# === End timing ===
end_time = time.time()
print(f"\n Total time taken by bot: {round(end_time - start_time, 2)} seconds")

