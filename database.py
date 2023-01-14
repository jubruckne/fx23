import pymysql.cursors
import database_settings

def Database:
    db: pymysql.Connection

    def __init__(self, server=None, user=None, pwd=None):
        self.server = server
        self.user = user
        self.pwd = pwd

        self.connect();


    def connect(self):
        self.db = pymysql.connect(host=self.server,
                                  port=3308,
                                  user=self.user,
                                  password=self.pwd,
                                  database='SSA',
                                  cursorclass=pymysql.cursors.DictCursor)

        try:
            # Create a cursor object
            cursor = self.db.cursor()

            # SQL Statement to create a database
            sql = "CREATE DATABASE SSA"

            # Execute the create database SQL statment through the cursor instance
            cursor.execute(sql)

            # SQL query string
            sql = "SHOW DATABASES"

            # Execute the sqlQuery
            cursor.execute(sql)

            # Fetch all the rows
            databaseList = cursor.fetchall()

            for db in databaseList:
                print(db)

        except Exception as e:
            print("Error: {}".format(e))

        finally:
            self.db.close()
