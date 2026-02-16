import json


'''Converta a string abaixo para dicionário usando json.loads():'''

produtos = {"produto": "Notebook", "preco": 3500}

json_produtos = json.dumps(produtos)
#convertendo json em dicionalrio
produtos_dict = json.loads(json_produtos)

print(produtos_dict)

