usuarios = []

def cadastrar_usuarios():
    print("\n=== Lista de Usúario")

    nome = input("Digite o nome: ")
    idade = input("Digite idade: ")
    email = input("Digite o email: ")

    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    usuarios.append(usuario)

    print("Usuário cadastrado com sucesso!")

def menu():
    while True:
        print("\n===== SISTEMA DE CADASTRO =====")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Excluir usuário")
        print("4 - Sair")

        opcao = input ("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuarios()
        
        elif opcao == "4":
            print("Fechando área de cadastro...")
            break
        else:
            print("Opção inválida!")


            
menu()