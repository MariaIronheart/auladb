from conexao import conectar

# chama a função conectar
conn = conectar()

# criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()

# solicitando a entrada do usuário
busca = input("Digite o nome do estado que deseja editar: ")

# executando a consulta com LIKE para verificar se o registro existe
sql = "SELECT * FROM estado WHERE nome LIKE %s"
val = ("%" + busca + "%",)
cursor.execute(sql, val)

# obtendo o resultado
result = cursor.fetchone()

# se o resultado não for nulo, o registro existe e pode ser editado
if result:
    codigo = result[0]
    nome_antigo = result[1]
    print(f"O nome atual do estado é '{nome_antigo}'.")
    novo_nome = input("Digite o novo nome do estado: ")

    # solicita as novas informações para o registro
    while not novo_nome:
        novo_nome = input("Digite o novo nome do estado: ")

    confirmacao = input(f"Tem certeza que deseja alterar o nome do estado '{nome_antigo}' para '{novo_nome}'? (s/n) ")

    # se a confirmação for positiva, atualiza o registro
    if confirmacao.lower() == "s":
        sql = "UPDATE estado SET nome = %s WHERE codigo = %s"
        val = (novo_nome, codigo)
        cursor.execute(sql, val)
        conn.commit()
        print(f"O nome do estado '{nome_antigo}' foi atualizado para '{novo_nome}' com sucesso!")
    else:
        print("Operação cancelada pelo usuário.")

# se o resultado for nulo, o registro não existe
else:
    print("Não foi encontrado nenhum estado com o nome informado.")

# fechar a conexão e o cursor
conn.close()