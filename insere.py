import mysql.connector

config = {
    'user': 'admin',
    'password': 'aulanoiteFaculdade',
    'host': 'dbaula.cp8xbhx2ises.us-east-1.rds.amazonaws.com',
    'database': 'aula'
}

try:
    conn = mysql.connector.connect(**config)
    print('Execução executada com sucesso')
except mysql.connector.Error as err:
    print(f'Conexão falhou: {err}')
    
cursor = conn.cursor()

nome_estado = input('Digite o nome do estado: ')
codigo_estado = input('Digite o código do estado: ')

sql = 'INSERT INTO estado (codigo,nome) VALUES (%s,%s)'
val = (codigo_estado, nome_estado)
cursor.execute(sql,val)

conn.commit()

print(cursor.rowcount , 'registro(s) inserido(s) com sucesso.')

conn.close()
