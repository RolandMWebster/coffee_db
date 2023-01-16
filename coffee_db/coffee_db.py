import psycopg2
import psycopg2.extras

from coffee_db.settings import DATABASE_URL


class CoffeeDB():
    """Class to represent the PSQL coffee database"""

    def __init__(self):

        self.db_url = DATABASE_URL

    def _connect(self):

        return psycopg2.connect(
            self.db_url
        )

    def _execute(self, query: str, values: tuple = None):

        with self._connect() as conn:
            cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cur.execute(query, values)

            try:
                output = cur.fetchall()
                output = [dict(row) for row in output]
            except psycopg2.ProgrammingError:
                output = None

            conn.commit()

        return output

    def _get_next_id(self, table: str):

        ids = self._execute(f"SELECT id from {table}")
        ids = [x["id"] for x in ids]

        return max(ids) + 1

    def insert_row(self, table: str, values: tuple):

        values = (self._get_next_id(table),) + values
        value_format = "%s, " * (len(values) - 1)

        query = """
            INSERT INTO {0}
            VALUES ({1}%s)
        """.format(table, value_format)

        self._execute(query, values)

    def remove_row(self, table: str, coffee_id: tuple):

        query = """
            DELETE FROM {0}
            WHERE id=%s
        """.format(table)

        self._execute(query, coffee_id)

    def get_data(self, table: str):

        query = f"SELECT * FROM {table}"

        return self._execute(query)
