aluno = {}
aluno["nome"] =  ["Artur"]
aluno["idade"] = [25]
aluno["curso"] = ["Engenharia de prompt"]   
aluno["nota"] = [10.0]


# Aluno 1
aluno1 = {}
aluno1["nome"] = ["Artur"]
aluno1["idade"] = [25]
aluno1["curso"] = ["Engenharia de prompt"]
aluno1["nota"] = [10.0]

# Aluno 2
aluno2 = {}
aluno2["nome"] = ["Beatriz"]
aluno2["idade"] = [22]
aluno2["curso"] = ["Engenharia de prompt"]
aluno2["nota"] = [9.5]

# Aluno 3
aluno3 = {}
aluno3["nome"] = ["Caio"]
aluno3["idade"] = [30]
aluno3["curso"] = ["Engenharia de prompt"]
aluno3["nota"] = [8.8]

# Aluno 4
aluno4 = {}
aluno4["nome"] = ["Diana"]
aluno4["idade"] = [28]
aluno4["curso"] = ["Engenharia de prompt"]
aluno4["nota"] = [9.2]

# Aluno 5
aluno5 = {}
aluno5["nome"] = ["Eduardo"]
aluno5["idade"] = [24]
aluno5["curso"] = ["Engenharia de prompt"]
aluno5["nota"] = [7.5]

# Aluno 6
aluno6 = {}
aluno6["nome"] = ["Fernanda"]
aluno6["idade"] = [27]
aluno6["curso"] = ["Engenharia de prompt"]
aluno6["nota"] = [10.0]

# Aluno 7
aluno7 = {}
aluno7["nome"] = ["Gabriel"]
aluno7["idade"] = [21]
aluno7["curso"] = ["Engenharia de prompt"]
aluno7["nota"] = [8.0]

# Aluno 8
aluno8 = {}
aluno8["nome"] = ["Helena"]
aluno8["idade"] = [26]
aluno8["curso"] = ["Engenharia de prompt"]
aluno8["nota"] = [9.7]

# Aluno 9
aluno9 = {}
aluno9["nome"] = ["Ítalo"]
aluno9["idade"] = [29]
aluno9["curso"] = ["Engenharia de prompt"]
aluno9["nota"] = [8.5]

# Aluno 10
aluno10 = {}
aluno10["nome"] = ["Júlia"]
aluno10["idade"] = [23]
aluno10["curso"] = ["Engenharia de prompt"]
aluno10["nota"] = [9.0]

lista_alunos = [aluno1, aluno2, aluno3, aluno4, aluno5, aluno6, aluno7, aluno8, aluno9, aluno10]

print(f"Digite o nome do aluno para buscar a nota: ")
nome_busca = input()
for aluno in lista_alunos:
    if aluno["nome"][0].lower() == nome_busca.lower():
        print(f"Nota do aluno {aluno['nome'][0]}: {aluno['nota'][0]}")
        break
else:
    print("Aluno não encontrado.")
maior_nota = 0
menor_nota = 10

for aluno in lista_alunos:

    if aluno["nota"][0] > maior_nota:
        maior_nota = aluno["nota"][0]
    if aluno["nota"][0] <menor_nota:
        menor_nota = aluno["nota"][0]
    
print('Maior nota: ', maior_nota)
print('Menor nota: ', menor_nota)
print('Média das notas: ', sum(aluno["nota"][0] for aluno in lista_alunos) / len(lista_alunos))

