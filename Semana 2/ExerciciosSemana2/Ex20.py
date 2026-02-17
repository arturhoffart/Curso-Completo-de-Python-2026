import json

'''Desafio Final (Mentalidade de API)
Crie um JSON simulando resposta de pagamento:
{
  "id": "pay_123",
  "status": "approved",
  "customer": {
      "name": "Artur",
      "email": "artur@email.com"
  },
  "items": [
      {"product": "Curso IA", "price": 997},
      {"product": "Mentoria", "price": 1997}
  ]
}

Depois:
Calcule o valor total
Imprima o email do cliente
Verifique se o pagamento está aprovado'''

resposta_pagamento = {
    "id": "pay_123",
    "status": "approved",
    "customer": {
        "name": "Artur",
        "email": "artur.hoffart@gmail.com"
    },
    "items": [
        {"product": "Curso IA", "price": 997},
        {"product": "Mentoria", "price": 1997}
    ]
}

resposta_json = json.dumps(resposta_pagamento, indent=4)
with open("resposta_pagamento.json", "w") as file:
    file.write(resposta_json)

#Calcular o valor total a partir de arquivo json
with open("resposta_pagamento.json", "r") as file:
    resposta_carregada = json.load(file)

#total = sum(item["price"] for item in resposta_carregada["itens"])
total = 0
for item in resposta_carregada["items"]:
    total += item["price"]


email_cliente = resposta_carregada["customer"]["email"]
status_pagamento = resposta_carregada["status"]

print(f'Valor total: {total:.2f}')
print(f'Email do cliente: {email_cliente}')
if status_pagamento.lower() == "approved":
    print("Pagamento aprovado!")
else:
    print("Pagamento não Aprovado.")

