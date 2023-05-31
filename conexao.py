import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
    host = 'dbaula.cp8xbhx2ises.us-east-1.rds.amazonaws.com',
    user ='admin',
    password = 'aulanoiteFaculdade',
    database = 'aula'
)

    return mydb