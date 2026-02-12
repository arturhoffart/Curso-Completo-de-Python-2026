
alunos = []

print("Cadastre 3 alunos: ")

for i in range(3):
    aluno = {}
    aluno["nome"] = input("Digite o nome do aluno: ")
    aluno["nota"] = float(input("Digite a nota do aluno: "))
    alunos.append(aluno)

print("\nLista de Alunos: ")
for aluno in alunos:
    print(aluno)