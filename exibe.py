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

sql = 'SELECT * FROM estado'
cursor.execute(sql)

result = cursor.fetchall()
print(result)

for linhas in result:
    print(linhas)
    
conn.close()