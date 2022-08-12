import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user="pypyUser",
                              password="urubu100", 
                              host="localhost", 
                              database="pypy", 
                              autocommit=True)

def insert(query): 
    try:
        cursor = cnx.cursor()
        cursor.execute(query)
    except mysql.connector.Error as error:
        print("ERRO {}".format(error))
    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()
            return cursor.rowcount

def select(query):
    try:
        cursor = cnx.cursor()
        cursor.execute(query)
        dados = cursor.fetchone()
        print("You're connected to database: ", dados)
    except mysql.connector.Error as error:
        print('Erro')
        dados = error
    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()
            return dados
