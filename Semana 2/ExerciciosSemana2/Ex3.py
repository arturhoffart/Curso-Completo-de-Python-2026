import json

'''
Crie um JSON representando:
Um aluno
Nome
Nota
Aprovado (True/False)
Converta para string JSON e imprima.
'''

aluno = {
    "nome": "artur",
    "nota": 9.5,
    "aprovado": True

}

aluno_json = json.dumps(aluno)
print(aluno_json)