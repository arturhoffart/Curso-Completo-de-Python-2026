import json
#Leia o arquivo criado no exercício anterior e imprima apenas os produtos com estoque maior que 0.

#open products.json and read the content
with open("products.json", 'r') as file:
    products_from_file = json.load(file)
    for product in products_from_file:
        if product["estoque"] > 0:
            print(product["nome"])
