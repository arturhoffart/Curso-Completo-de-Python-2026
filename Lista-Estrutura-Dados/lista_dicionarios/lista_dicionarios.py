alunos = []

for i in range(3):
    aluno = {}
    aluno["nome"] = input("digite o nome do aluno: ")
    aluno["nota"] = float(input('digite a nota do aluno: '))
    alunos.append(aluno)

print('Lista de Alunos: ')
for aluno in alunos:
    print(aluno["nome"], ":", aluno["nota"])

    