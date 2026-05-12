import pymysql
def get_connection():
    connecction=pymysql.connect(
        host='localhost',
        user='root',
        password='Jagadeeshmysql',
        database='yuvasmik'
    )
    return connecction
def get_connection1():
    connecction=pymysql.connect(
        host='localhost',
        user='root',
        password='Jagadeeshmysql'
    )
    return connecction