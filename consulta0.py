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

busca= input('Digite o nome que deseja buscar: ')

sql = "SELECT * FROM estado WHERE nome LIKE %s"
val = ('%' + busca + '%',)
cursor.execute(sql,val)

results = cursor.fetchall()

for result in results:
    print(result)
    
conn.close()