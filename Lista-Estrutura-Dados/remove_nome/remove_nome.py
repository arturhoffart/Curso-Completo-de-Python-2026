nomes = ["Artur", "Fausto", "Juliano", "flavio", "Michel"]
print(nomes)

nome = input("Digite um nome para remover: ")
if nome in nomes:
    nomes.remove(nome)
    print("Nome removido com sucesso!")
else:
    print("Nome não encontrado na lista.")

print(nomes)