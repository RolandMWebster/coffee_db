import os

import pandas as pd
import psycopg2

DATABASE_URL = os.environ.get("DATABASE_URL")


class CoffeeDB():
    """Class to represent the PSQL coffee database"""

    def __init__(self):

        self.db_url = DATABASE_URL
    
    def _connect(self):

        return psycopg2.connect(
            self.DATABSE_URL
        ).cursor()

    def get_data(self):

        query = "SELECT * FROM test_coffee"

        with self._connect() as con:
            return pd.read_sql(query, con)

    def insert_coffee(self, values: tuple):

        query = """
            INSERT INTO test_coffee (id, Roastery, Country)
            VALUES (%s)
        """

        with self._connect() as con:
            con.execute(query, values)
