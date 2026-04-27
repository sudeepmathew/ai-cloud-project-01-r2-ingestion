import boto3
import os
import uuid
from dotenv import load_dotenv

load_dotenv()

r2 = boto3.client(
    "s3",
    endpoint_url=f"https://{os.getenv("R2_ACCOUNT_ID")}.r2.cloudflarestorage.com",
    aws_access_key_id=os.getenv("R2_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("R2_SECRET_KEY"),
)

def upload_to_r2(file):

    key = f"raw/profiles/{uuid.uuid4()}-{file.name}"

    r2.upload_fileobj(file, os.getenv("R2_BUCKET"), key)

    return key

   