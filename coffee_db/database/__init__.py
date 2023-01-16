import os

from coffee_db.database.config import config

if "DATABASE_URL" in os.environ.keys():
    DATABASE_URL = os.environ["DATABASE_URL"]
else:
    DATABASE_URL = config()
