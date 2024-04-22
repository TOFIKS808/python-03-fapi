# pylint: disable=R0801, R0903
"""
     Testy tworzenia bazy danych oraz populacji danych do utworzonej bazy
"""

import unittest
from os import getenv
from tests.test_db_abstract import TestDbAbstractTestCase

db_name = getenv('PG_DB_NAME_TEST')
db_user = getenv('PG_DB_USER')
db_pass = getenv('PG_DB_PASS')
db_host = getenv('PG_DB_HOST')
db_port = getenv('PG_DB_PORT')
URL = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"


class PostgresTestCase(TestDbAbstractTestCase):
    """Testing class"""

    @unittest.skip
    def test_all(self):
        """ Testing all remade functions in Postgres """

        self.func_create_db(URL)
        self.func_create_schema(URL)
        self.func_endpoint_users(URL)
        self.func_endpoint_posts(URL)
        self.func_endpoint_comments(URL)
        self.func_endpoint_albums(URL)
        self.func_endpoint_photos(URL)
        self.func_endpoint_todos(URL)


if __name__ == '__main__':
    unittest.main()
