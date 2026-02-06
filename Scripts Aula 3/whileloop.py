# == while loop ==
# usado para loops dependentes de condição

# publicar um produto com comissão de 10% se for acima de R$ 20,00

valor = float(input('Digite o valor do produto: R$ '))

while valor > 20:
    valor = valor + (valor * 0.10)
    break

print(f'O valor final do seu produto será de R$ {valor:.2f}')
