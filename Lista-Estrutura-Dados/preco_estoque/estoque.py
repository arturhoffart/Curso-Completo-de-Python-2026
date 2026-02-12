print(f'🟡 EXERCÍCIO 6 — Dicionário Básico')
'''
Crie um dicionário representando um produto:
nome
preço
quantidade
Mostre o valor total em estoque (preço × quantidade).
'''

produto = {

    "nome": "Caranguejo",
    "preco": 25.99,
    "quantidade": 23
}
print(f'valor total em estoque: R$ {produto["preco"] * produto["quantidade"]:.2f}')

