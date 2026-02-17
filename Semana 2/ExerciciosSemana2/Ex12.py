import json
'''Modifique o sistema anterior para:

Ao iniciar o programa, carregar o arquivo JSON existente

Não apagar os dados antigos'''



users = []
while True:
    name = input("Digite o nome do usuário (ou 'sair' para encerrar)" )
    if name.lower() == 'sair':
        break
    age = int(input("Digite a idade do usuário: "))
    user = {"nome": name, "idade": age}
    users.append(user)
    with open("users.json", 'w') as file:
        json.dump(users, file, indent=4)
        
try:
    with open("users.json", 'r') as file:
        existing_users = json.load(file)
        users.extend(existing_users)
except FileNotFoundError:
    pass

