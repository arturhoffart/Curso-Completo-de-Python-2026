import json
'''Crie uma lista de produtos:
nome
preco
estoque
Converta para JSON formatado (indent=4) e salve em arquivo.'''

products = [
    {"nome": "notebook", "preco": 3500, "estoque": 10},
    {"nome": "smartphone", "preco": 2000, "estoque": 20},
    {"nome": "tablet", "preco": 1500, "estoque": 15}
]

products_json = json.dumps(products, indent=4)
with open("products.json", 'w') as file:
    file.write(products_json)


