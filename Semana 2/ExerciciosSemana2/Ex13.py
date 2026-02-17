import json

'''Crie um JSON com:
Uma empresa
Lista de funcionários
Cada funcionário tem:
nome
cargo
salário
Imprima apenas os salários.'''

empresa = {
    "nome": "A2H Solutions",
    "funcionarios": [
        {"nome": "Artur", "cargo": "CEO", "salario": 10000},
        {"nome": "Maria", "cargo": "CTO", "salario": 9000},
        {"nome": "João", "cargo": "Developer", "salario": 5000}
    ]
}

empresa_json = json.dumps(empresa)
print(empresa_json)

#acessando os salários
empresa_dict = json.loads(empresa_json)
for funcionario in empresa_dict["funcionarios"]:
    print(funcionario["salario"])

    