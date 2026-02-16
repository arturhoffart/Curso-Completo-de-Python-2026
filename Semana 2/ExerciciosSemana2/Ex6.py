import json
'''Crie uma lista de dicionários representando 3 usuários:

nome

idade

Converta tudo para JSON.'''

usuarios = [
    {"nome": "artur", "idade": 44},
    {"nome": "maria", "idade": 30},
    {"nome": "joão", "idade": 25}
    ]

usuarios_json = json.dumps(usuarios)
print(usuarios_json)

