from conexao import conectar
def listar(conn,cursor):
    conn = conectar()
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM estado")
    
    resultados = cursor.fetchall()
    
    for resultado in resultados:
        print(resultado)
    
    cursor.close()
    
    conn.close()
    
def inserir(codigo,nome):
    conn = conectar()
    cursor = conn.cursor
    
    sql = "INSERT INTO estado (codigo, nome) VALUES (%s,%s)"
    val = (codigo,nome)
    cursor.execute(sql,val)
    
    conn.commit()
    
    print('Registro inserido com sucesso.')
    
    cursor.close()
    conn.close()
    
def atualizar(codigo, novo_nome):
    conn = conectar()
    cursor = conn.cursor()
    
    sql = 'UPDATE estado SET nome = %s WHERE codigo = %s'
    val = (novo_nome, codigo)
    cursor.execute(sql,val)
    conn.commit()
    #verificar se algum registro foi atualizado
    if cursor.rowcount == 0:
     print('Nenhum registro atualizado.')
    else: 
     print('Registro atualizado com sucesso.')
    cursor.close()
    conn.close()
    
def deletar(codigo):
    conn = conectar()
    cursor = conn.cursor
    sql = 'DELETE FROM estado WHERE codigo = %s'
    val = (codigo,)
    cursor.execute(sql,val)
    
    conn.commit()
    
    if cursor.rowcount == 0:
     print('Nenhum registro deletado')
    else:
     print('Registro deletado com sucesso')
    cursor.close()
    conn.close()
    
conn = conectar()
cursor = conn.cursor()
while True:
    print('O que você deseja fazer?')
    print('1- Listar estados')
    print('2- Inserir novo estado')
    print('3- Atualizar um estado')
    print('4- Deletar um estado')
    print('0- Sair')
    opcao = int(input('Digite o número da opção desejada'))
    
    if opcao == 1:
        listar(conn, cursor)
     
    elif opcao == 2:
        codigo = int(input('Digite o código do novo estado: '))
        nome = input('Digite o nome do novo estado: ')
        inserir(codigo, nome)
        
    elif opcao == 3:
        codigo = int(input('Digite o código do estado que deseja: '))
        nome = input('Digite o novo nome do estado: ')
        atualizar(codigo,nome)
    
    elif opcao == 4:
        codigo = int(input('Digite o código do estado que deseja: '))
        deletar(codigo)
        
    elif opcao == 0:
        break
    
    else:
        print('Opção inválida, digite novamente.')