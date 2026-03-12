import json

def carregar_usuarios():
    try:
        with open("usuarios.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return[]
    
def salvar_usuarios(usuarios):
    with open("usuarios.json", "w") as arquivo: 
        json.dump(usuarios, arquivo, indent=4) # Converte a lista Python em JSON

usuarios = carregar_usuarios()

def cadastrar_usuarios():
    print("\n=== Lista de Usúario ===")

    nome = input("Digite o nome: ")
    idade = input("Digite idade: ")
    email = input("Digite o email: ")

    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    usuarios.append(usuario)

    salvar_usuarios(usuarios)

    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    print("===== Lista de Usuarios =====")

    if not usuarios:
        print("Sem usuário cadastrado!")
        return
    
    for i, usuario in enumerate(usuarios, start=1):
        print(f"\nUsuário {i}")
        print(f"Nome: {usuario['nome']}")
        print(f"Idade: {usuario['idade']}")
        print(f"Email: {usuario['email']}")

def excluir_usuario():
    listar_usuarios()

    indice = int(input("\nDigite o número de usuários para excluir: "))
    
    if 1 <= indice <= len(usuarios):
        usuarios.pop(indice - 1)
        salvar_usuarios(usuarios)
        print("Usuário removido com sucesso!")
    else:
        print("Usuário inválido")

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