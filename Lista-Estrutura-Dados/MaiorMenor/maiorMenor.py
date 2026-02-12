for i in range(5):
    numero = int(input('Digite um número: '))
    if i ==0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print('O maior número é: ', maior)
print('O menor número é: ', menor)
