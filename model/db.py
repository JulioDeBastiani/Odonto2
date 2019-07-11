from peewee import MySQLDatabase

def get_db():
    return MySQLDatabase('Odonto', host='localhost', port=3306, user='root', passwd='3Ewu85B8bB')