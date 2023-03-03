import os

from coffee_db.database.config import config
from coffee_db.database.aws_utils import get_aws_url


ENVIRONMENT = os.environ.get("ENVIRONMENT", "LOCAL")

if ENVIRONMENT == "HEROKU":
    DATABASE_URL = os.environ["DATABASE_URL"]
elif ENVIRONMENT == "AWS":
    DATABASE_URL = get_aws_url()
elif ENVIRONMENT == "LOCAL":
    DATABASE_URL = config()
