import mysql.connector

class DbUtils(object):
    def __init__(self):
        # self.config = {
        #     'user': 'root',
        #     'password': 'root',
        #     'host': 'db',
        #     'port': '3306',
        #     'database': 'elibrary'
        # }

        self.config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'port': '3306',
            'database': 'elibrary',
            'auth_plugin': 'mysql_native_password'
        }


    # for selects
    def query(self, sql, dbfilter = None):
        connection = mysql.connector.connect(**self.config)
        cursor = connection.cursor(buffered=True, dictionary=True)
        if dbfilter is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, dbfilter)
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        return rows

    # for inserts, updates, deletes
    def execute(self, sql, data):
        connection = mysql.connector.connect(**self.config)
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        cursor.close()
        connection.close()
        return cursor.lastrowid