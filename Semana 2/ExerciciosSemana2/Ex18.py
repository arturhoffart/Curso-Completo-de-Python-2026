import json

#lendo arquivo usuarios
try:
    with open("usuarios.json", "r") as file:
        dados = json.load(file)
        usuarios = dados["usuarios"]

except FileNotFoundError:
    print("Arquivo não encontrado.")
    usuarios = []

#Função para buscar usuário
def buscar_usuario(nome_busca, usuarios):
    for usuario in usuarios:
        if usuario["nome"].lower() == nome_busca.lower():
            return usuario

    return None

nome_busca = input("Digite o nome para busca: ")
resultado = buscar_usuario(nome_busca, usuarios)
print(usuarios)
print(type(usuarios))
if resultado:
    print(f'Usuário encontrado: {resultado}')
else:
    print("Usuário não encontrado.")




'''
Crie um sistema que:
Leia um arquivo JSON com usuários
Permita buscar por nome
Retorne o usuário encontrado



FILE_NAME = "usuarios.json"


def carregar_usuarios():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return []


def buscar_usuario(nome_busca, usuarios):
    for usuario in usuarios:
        if usuario["nome"].lower() == nome_busca.lower():
            return usuario
    return None


def main():
    usuarios = carregar_usuarios()

    if not usuarios:
        print("Nenhum usuário disponível.")
        return

    nome = input("Digite o nome para buscar: ")

    resultado = buscar_usuario(nome, usuarios)

    if resultado:
        print("Usuário encontrado:")
        print(resultado)
    else:
        print("Usuário não encontrado.")


if __name__ == "__main__":
    main()
'''