import psycopg2
import psycopg2.extras

from coffee_db.database import DATABASE_URL


class CoffeeDB():
    """
    Class to represent the PSQL coffee database
    """

    def __init__(self):

        self.db_url = DATABASE_URL

    def _connect(self) -> psycopg2.extensions.connection:
        """
        Generate a psycopg2 connection object.
        """

        return psycopg2.connect(self.db_url)

    def _execute(self, query: str, values: tuple = None) -> list[dict]:
        """
        Executre sql commands, given a query.
        """

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

    def _get_next_id(self, table: str) -> int:
        """
        Generate the next unique_id for a given table.
        """

        ids = self._execute(f"SELECT id from {table}")
        ids = [x["id"] for x in ids]

        return max(ids) + 1

    def insert_row(self, table: str, values: tuple) -> None:
        """
        Insert values into a new row of a given table.
        """

        values = (self._get_next_id(table),) + values
        value_format = "%s, " * (len(values) - 1)

        query = """
            INSERT INTO {0}
            VALUES ({1}%s)
        """.format(table, value_format)

        self._execute(query, values)

    def remove_row(self, table: str, row_id: tuple) -> None:
        """
        Remove a row from a given table, based on the id.
        """

        query = """
            DELETE FROM {0}
            WHERE id=%s
        """.format(table)

        self._execute(query, row_id)

    def get_data(self, table: str) -> list[dict]:
        """
        Get all data from a given table.
        """

        query = f"SELECT * FROM {table}"

        return self._execute(query)
