import json
import certbot.main
import os
import boto3

WORKDIR="/tmp/certbot"
EMAIL="example@gmail.com"
DOMAIN="example.com"
DOMAIN2="www.example.com"

BUCKET="example-s3bucket"
REGION="example-region"
KEY="ssl"


def upload_certs():
    client = boto3.client('s3', REGION)
    cert_dir = os.path.join(WORKDIR, 'live')
    for dirpath, _dirnames, filenames in os.walk(cert_dir):
        for filename in filenames:
            local_path = os.path.join(dirpath, filename)
            relative_path = os.path.relpath(local_path, cert_dir)
            # 'folder' to upload certificate to
            s3_key = os.path.join(KEY, relative_path)
            client.upload_file(local_path, BUCKET, s3_key)

def lambda_handler(event, context):
    # get certificate
    certbot.main.main(["certonly", "--dry-run", "--work-dir", WORKDIR, "--config-dir", WORKDIR, "--logs-dir", WORKDIR, "--non-interactive", "--agree-tos", "--email", EMAIL, "--dns-route53", "-d", DOMAIN, "-d", DOMAIN2])


    # upload the certificate to s3 bucket
    upload_certs()
    
    return  {
        'headers': {'Content-Type' : 'application/json'},
        'statusCode': 200,
        'body': json.dumps({"message": "SSL renewed", "event": event})
    }
