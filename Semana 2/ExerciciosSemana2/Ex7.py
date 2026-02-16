import json
#7️⃣ A partir da lista acima, imprima apenas os usuários com idade maior que 25.

usuarios = [
    {"nome": "artur", "idade": 44},
    {"nome": "maria", "idade": 30},
    {"nome": "joão", "idade": 25}
    ]

usuarios_json = json.dumps(usuarios)
print(usuarios_json)

usuarios_dict = json.loads(usuarios_json)
for usuario in usuarios_dict:
    if usuario["idade"] > 25:
        print(usuario["nome"])

