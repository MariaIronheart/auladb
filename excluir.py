from conexao import conectar

conn = conectar()

cursor = conn.cursor()

busca = input('Digite o nome que deseja bsucar: ')

sql = 'SELECT * FROM estado WHERE nome LIKE %s'
val = ('%'+busca+'%',)
cursor.execute(sql,val)

result = cursor.fetchone()
if result:
    codigo = result[0]
    nome = result[1]
    confirmacao = input(f"Tem certeza que deseja deletar o estado'{nome}'? (s/n)")
    if confirmacao.lower() == 's':
        sql = 'DELETE FROM estado WHERE codigo = %s'
        val = (codigo,)
        cursor.execute(sql,val)
        conn.commit()
        print(f"O estado'{nome}'foi deletado com sucesso!")
    else:
        print('Operação cancelada pelo usuário.')
else: 
 print('Não foi encontrado nenhum estado com o nome informado.')

conn.close()