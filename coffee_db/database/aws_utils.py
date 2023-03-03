import json

import boto3
from botocore.exceptions import ClientError


def get_db_secrets():
    """Get secrets for the AWS RDS Database from the AWS Secret Store"""

    secret_name = "rds!db-94e699a5-222e-44ef-9886-c4f607e847f3"
    region_name = "eu-west-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    secret_string = get_secret_value_response['SecretString']
    secret_dict = json.loads(secret_string)

    return secret_dict


def get_aws_url():
    """Build the connection credentials for the AWS Database"""

    secrets = get_db_secrets()

    return (
        "host=database-1.c20cskzjaq5p.eu-west-2.rds.amazonaws.com"
        " dbname=postgres"
        f" user={secrets['username']}"
        f" password={secrets['password']}"
        " port=5432"
    )
