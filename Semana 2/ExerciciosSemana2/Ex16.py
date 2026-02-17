import json
'''Crie um sistema que:
Salve logs de ações em um arquivo JSON
Cada log deve ter:
usuario
acao
timestamp (pode ser string simples)'''

log = {
    "usuario" : "artur",
    "acao" : "login",
    "timestamp" : "2024-06-01 10:00:00"
}

log_json = json.dumps(log, indent=4)
with open("log.json", 'w') as file:
    file.write(log_json)




