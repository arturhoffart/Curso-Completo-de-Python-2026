import json

'''Crie um JSON representando uma conversa de IA:
{
  "messages": [
      {"role": "user", "content": "Olá"},
      {"role": "assistant", "content": "Como posso ajudar?"}
  ]
}


Acesse a última mensagem.'''

conversa = {
    'messages': [
        {"role": "user", "content": "olá"},
        {"role": "assistant", "content": "como posso ajudar?"},
        {"role": "user", "content": "qual é a capital da França?"}
    ]
}

conversa_json = json.dumps(conversa)

with open("conversa.json", "w") as f:
    f.write(conversa_json)

# Acessar a última mensagem
ultima_mensagem = conversa["messages"][-1]
print(ultima_mensagem)

