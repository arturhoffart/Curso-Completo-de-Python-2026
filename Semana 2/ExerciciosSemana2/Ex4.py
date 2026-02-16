import json

#Crie um JSON com uma lista de 3 números.

#Converta para dicionário Python e imprima o segundo número.
numeros_json = '[10, 20, 30]'
numeros_dict = json.loads(numeros_json)
print(numeros_dict[1])

