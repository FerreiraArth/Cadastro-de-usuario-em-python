import json

def carregar_usuarios():
    try:
        with open("usuarios.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return[]

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

def listar_usuarios():
    print("===== Lista de Usuarios =====")

    if len(usuarios) == 0:
        print("Sem usuário cadastrado!")
        return
    
    for i, usuario in enumerate(usuarios, start=1):
        print(f"\nUsuário {i}")
        print(f"Nome: {usuario['nome']}")
        print(f"Idade: {usuario['idade']}")
        print(f"Email: {usuario['email']}")

def excluir_usuario():
    listar_usuarios()

    if len(usuarios) == 0:
        return
    
    try:
        indice = int(input("\nDigite o número de usuários para excluir: "))

        if 1 <= indice <= len(usuarios):
            usuarios.pop(indice - 1)
            print("Usuário removido com sucesso!")
        
        else:
            print("Usuário inválido")
    except ValueError:
        print("Digite um número válido.")

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

        elif opcao == "2":
            listar_usuarios()
            
        elif opcao == "4":
            print("Fechando área de cadastro...")
            break

        elif opcao == "3":
            excluir_usuario()

        else:
            print("Opção inválida!")

            
menu()