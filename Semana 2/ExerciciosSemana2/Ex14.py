import json
'''Crie um JSON representando um carrinho de compras.

Depois:

Calcule o valor total usando os dados carregados do JSON.'''

compras = {
    "produtos": [
        {"nome": "camisa", "preço": 50.0, "quantidade": 2},
        {"nome": "calça", "preço": 100.0, "quantidade": 1},
        {"nome": "sapato", "preço": 150.0, "quantidade": 1}

    ]
}

compras_json = json.dumps(compras)
print(compras_json)

#calculando o valor total usando os dados carregados do carrinho
compras_dict = json.loads(compras_json)
total = 0
for produto in compras_dict["produtos"]:
    total += produto["preço"] * produto["quantidade"]
print(f"valor total: {total:.2f}")

