import pymysql.cursors
import database_settings


class Database:
    connection: pymysql.Connection
    cursor: pymysql.cursors.Cursor

    def __init__(self, server=None, port=None, dbname=None, user=None, pwd=None):
        if server is None:
            self.server = database_settings.server
        else:
            self.server = server

        if port is None:
            self.port = database_settings.port
        else:
            self.port = port

        if dbname is None:
            self.dbname = database_settings.dbname
        else:
            self.dbname = dbname

        if user is None:
            self.user = database_settings.user
        else:
            self.user = user

        if pwd is None:
            self.pwd = database_settings.pwd
        else:
            self.pwd = pwd

    def connect(self):
        self.connection = pymysql.connect(host=self.server,
                                          port=self.port,
                                          user=self.user,
                                          password=self.pwd,
                                          database=self.dbname,
                                          cursorclass=pymysql.cursors.DictCursor)

        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute("SHOW DATABASES")

            for db in self.cursor.fetchall():
                print(db)

        except Exception as e:
            print("Error: {}".format(e))

        finally:
            self.connection.close()

    def create(self):
        # SQL Statement to create a database
        sql = "CREATE DATABASE SSA"

        # Execute the create database SQL statment through the cursor instance
        self.cursor.execute(sql)
