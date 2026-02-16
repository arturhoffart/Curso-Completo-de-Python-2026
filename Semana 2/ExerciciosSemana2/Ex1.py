import json

'''
Crie um dicionário Python representando:
nome
idade
email
Depois converta para JSON usando json.dumps().
'''
usuario = {
    "nome": "artur",
    "idade": 44,
    "e-mail": "artur.hoffart@gmail.com"
}

#convertendo dicionario em json
json_usuario = json.dumps(usuario)
