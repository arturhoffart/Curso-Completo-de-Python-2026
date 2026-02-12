
lista = []
for i in range(5):
    lista.append(int(input('Digite um número: ')))

print(lista)

for numero in lista:
    soma = 0
    soma += numero
print('A soma da lista é: ', soma)

print('A média da lista é : ', soma/len(lista))

