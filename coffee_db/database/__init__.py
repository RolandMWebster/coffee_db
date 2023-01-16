import os

from coffee_db.database.config import config


DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    config(),
)
