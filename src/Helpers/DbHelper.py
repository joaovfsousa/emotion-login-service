import os
import pymysql

DB_HOST = os.environ["DB_HOST"]
DB_NAME = os.environ["DB_NAME"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]


class DbHelper:
    def __init__(self):
        self.connection = pymysql.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
        )

    def __del__(self):
        self.connection.close()

    def getCursor(self):
        return self.connection.cursor()
