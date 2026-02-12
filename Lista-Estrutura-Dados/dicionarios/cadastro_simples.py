aluno = {}


aluno["nome"] = input("Digite o nome do aluno: ")
aluno["idade"] = int(input("Digite a idade do aluno: "))
aluno["curso"] = input("digite o curso do aluno: ")
aluno["cidade"] = input("digite a cidade do aluno: ")

print("\nDados Cadastrados: ")

for chave in aluno:
    print(chave, ":", aluno[chave])

