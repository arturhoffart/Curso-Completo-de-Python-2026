import json

'''Crie um JSON com estrutura profundamente aninhada (3 níveis).

Depois acesse um valor interno específico.'''

dados = {
    "nivel1": {
        "nivel2": {
            "nivel3": "Estou no terceiro nível!"
        }
    }
}

dados_json = json.dumps(dados)
with open("dados.json", "w") as file:
    file.write(dados_json)

#Acessar o arquivo json
with open("dados.json", "r") as file:
    dados_carregados = json.load(file)

#Acessar o valor interno
valor_n3 = dados_carregados["nivel1"]["nivel2"]["nivel3"]
print(valor_n3)