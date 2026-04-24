import pymysql
import logging

class MySQLClient:
    def __init__(self, host, database, user, password, port=3306):
        try:
            self.connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=port,
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.connection.cursor()
            logging.info("MySQL Connection Successful")
        except Exception as e:
            logging.error(f"Error connecting to MySQL: {e}")
            raise

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            logging.info("Query executed successfully")
        except Exception as e:
            logging.error(f"Error executing query: {e}")
            self.connection.rollback()
            raise

    def fetch_all(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            logging.error(f"Error fetching data: {e}")
            raise

    def connection_close(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            logging.info("MySQL Connection Closed")
