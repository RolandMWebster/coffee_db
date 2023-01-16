import os

# grab the heroku URL, else use the local one
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "dbname=postgres"
)
