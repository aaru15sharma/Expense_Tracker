import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    passwd="root"
)

my_cursor = db.cursor()

my_cursor.execute("CREATE DATABASE test")