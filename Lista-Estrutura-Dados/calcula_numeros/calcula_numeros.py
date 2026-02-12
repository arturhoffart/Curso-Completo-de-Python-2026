numeros = []
soma =0
media = 0
while True:
    try:
        numero = int(input("Digite um número inteiro (ou -1 para sair): "))
        if numero == -1:
            break
        else:
            numeros.append(numero)
            soma = soma + numero
            media = soma / len(numeros)
    except ValueError:
        print("Valor inválido, por favor digite um número inteiro ou -1 para sair.")
print(f'A soma dos números é: {soma}')
print(f'A média dos números é: {media}')
print(f'A lista completa é: {numeros}')
