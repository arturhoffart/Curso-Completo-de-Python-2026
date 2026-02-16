import json

'''Crie um JSON aninhado com:
cliente
nome
cpf
pedidos (lista com 2 pedidos)
Acesse o nome do cliente e o primeiro pedido.'''

cliente = {
    "nome": "artur",
    "cpf": "12345678901",
    "pedidos": [
        {"id": 1, "valor": 100},
        {"id": 2, "valor": 200}
    ]

}
cliente_json = json.dumps(cliente)
print(cliente_json)

#acessando o nome do cliente e o primeiro pedido
cliente_dict = json.loads(cliente_json)
print(cliente_dict["nome"])
print(cliente_dict["pedidos"][0])
