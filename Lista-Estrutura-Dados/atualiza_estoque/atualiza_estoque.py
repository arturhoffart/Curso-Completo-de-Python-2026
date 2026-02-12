print(f'🟡 EXERCÍCIO 7 — atualiza estoque')
'''
Atualize o preço de um produto em estoque.
'''

produto = {

    "nome": "Caranguejo",
    "preco": 25.99,
    "quantidade": 23
}
print(f'valor total em estoque: R$ {produto["preco"] * produto["quantidade"]:.2f}')
novo_preco = float(input("Digite o novo preço do produto: "))
produto["preco"] = novo_preco
print(f'Valor do estoque atualizado é: R$ {produto["preco"] * produto["quantidade"]:.2f}')


