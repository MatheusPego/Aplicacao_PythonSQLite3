# Importo a biblioteca para funcionar de forma automática
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('produtos.db')
cur = conn.cursor()

# Interação com o usuário
while True:
    print("\nSelecione uma ação:")
    print("1 - Ver todos os dados")
    print("2 - Ver um dado específico")
    print("3 - Atualizar um dado")
    print("4 - Deletar um dado")
    print("5 - Sair")

    escolha = input("Digite o número da ação desejada: ").strip()

    if escolha == "1":
        cur.execute("SELECT * FROM clientes")
        resultados = cur.fetchall()
        print("Clientes encontrados:")
        for resultado in resultados:
            print(resultado)
    elif escolha == "2":
        empresa = input("Digite o nome da Empresa que deseja consultar: ").strip()
        cur.execute("SELECT * FROM clientes WHERE Empresa = ?", (empresa,))
        resultados = cur.fetchall()
        if resultados:
            print("Cliente(s) encontrado(s):")
            for resultado in resultados:
                print(resultado)
        else:
            print("Nenhum cliente encontrado com esse nome.")
    elif escolha == "3":
        id_atual = input("Digite o ID do cliente que deseja atualizar: ").strip()
        novo_id = input("Digite o novo ID: ").strip()
        novo_cliente = input("Digite o novo nome da Empresa: ").strip()
        nova_demanda = input("Digite a nova Demanda: ").strip()
        novo_venc = input("Digite o novo Vencimento: ").strip()
        cur.execute("UPDATE clientes SET id = ?, Empresa = ?, Demanda = ?, Vencimento = ? WHERE id = ?", 
                    (novo_id, novo_cliente, nova_demanda, novo_venc, id_atual))
        conn.commit()
        print("Registro atualizado com sucesso.")
    elif escolha == "4":
        id = input("Digite o ID do cliente que deseja deletar: ").strip()
        cur.execute("DELETE FROM clientes WHERE id = ?", (id,))
        conn.commit()
        print("Registro deletado com sucesso.")
    elif escolha == "5":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")

# Encerrando conexão com o Banco de Dados
conn.close()