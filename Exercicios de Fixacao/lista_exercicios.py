print('Exercícios de Fixação')
print('Lista nível fácil exercícios de 1 a 5 ')
'''
Olá Usuário
Crie um programa que:
Pergunte o nome do usuário
Imprima: "Bem-vindo, NOME"
'''

print('Exercício 1')
nome = input('Digite seu nome: ')
print(f'Bem-vindo, {nome}')

'''
Idade em 10 anos
Peça a idade do usuário e mostre:
"Daqui a 10 anos você terá X anos"
'''
idade = int(input('Digite sua idade: '))
idade = idade +10
print(f'daqui a 10 anos voce terá {idade} anos')

'''
3️⃣ Dobro do número

Peça um número e mostre o dobro dele.
'''
numero = float(input('Digite um número: '))
dobro = numero *2
print(f'O dobro de {numero} é {dobro}')

'''
4️⃣ Verificação de maioridade

Peça a idade e diga:

"Maior de idade"

"Menor de idade"
'''
idade2 = int(input('Digite sua idade: '))
if idade2 >= 18:
    print('Maior de idade')
else:
    print('Menor de idade.')

'''
5️⃣ Número positivo ou negativo

Peça um número e diga se ele é:
Positivo
Negativo
Zero
'''
numero2 = float(input('Digite um número: '))
if numero2 > 0:
    print('Positivo')
elif numero2 < 0:
    print ('Negativo')
else:
    print('Zero')


print('Lista 2 nível médio, exercícios de 6 a 10')
print('Condições + Loops')


print(f'6: Use um for para imprimir números de 1 a 10.')
for i in range(1, 11):
    print(i)
print(' ')

print(' ')
print('Exercídio 7: Numeros pares até 20')
for i in range(0, 21,2):
    print(i)

print('')
print('Exercício 8: Contador REgressivo de 10 até 1 com while')
contador = 10
while contador >=1:
    print(contador)
    contador -=1

print('')
print('Exercício 9: Use um loop para somar todos os números de 1 até 100. \n Mostre o resultado final.')
numero5 = 0
for i in range (1,101):
    numero5+=i
print(f'A soma de todos os números de 1 a 100 é {numero5}')

print('')
print('Exercício 10: Tabuada')
print('Peça um número e imprima a tabuada dele de 1 a 10.')
numero6 = int(input('Digite um número para ver a tabuada: '))
for i in range(1,11):
    resultado = numero6 * i
    print(f'{numero6} x {i} = {resultado}')

print(' ')
print(f'NÍVEL 3 – Funções (Muito Importante)')
print('1️⃣1️⃣ Função de saudação')
print(' ')
print('Crie uma função que receba um nome e imprima:')
print('"Olá, NOME!"')
def saudacao(nome):
    print(f'Olá, {nome}!')
nome2 = input('Digite seu nome: ')
saudacao(nome2)

print(' ')
print('1️⃣2️⃣ Função de soma')
print('Crie uma função que receba dois números e retorne a soma.')
print(' ')
print('Soma de dois numeros')
print('Função de soma')
print(f'Crie uma função que receba dois números e retorne a soma.')
numero3 = float(input('digite o primeiro numero'))
numero4 = float(input('digite o segundo numero'))
def soma(a, b):
    return a + b
resultado = soma(numero3, numero4)
print(f'A soma de {numero3} e {numero4} é {resultado}')

print(' ')
print(f'1️⃣3️⃣ Função que verifica maioridade')
print('Crie uma função que receba idade e retorne:')
print('True se for maior de idade')
print('False se não for')
def verifica_maioridade(idade):
    if idade>=18:
        return True
    else:
        return False
idade3 = int(input('digite sua idade: '))

print(f'1️⃣4️⃣ Calculadora simples')
print('Crie uma função que receba:')
print('número1')    
print('número2')
print('operação (+, -, *, /)')
print('E retorne o resultado.')

def calculadora(numero1, numero2, operacao):
    if operacao == '+':
        return numero1 + numero2
    elif operacao == '-':
        return numero1 - numero2
    elif operacao == '*':
        return numero1 * numero2
    elif operacao == '/':
        if numero2 !=0:
            return numero1 / numero2
        else:
            return 'Erro: Divisão por zero'
    else:
        return 'Operação inválida'
print('Calculadora Simples')
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
operacao = input('Digite a operação (+, -, *, /): ')
resultado = calculadora(numero1, numero2, operacao)
print(f'O resultado de {numero1} {operacao} {numero2} é: {resultado}')

print(' ')

print(f'🔴 NÍVEL 4 – Desafios (Combinação de Tudo)')
print(f'1️⃣5️⃣ Sistema de Login Simples')
print('Defina:')
print('usuario_correto = "admin"')
print('senha_correta = "1234"')
print(' ')
print('Peça usuário e senha.')
print('Se estiver correto → "Acesso permitido"')
print('Senão → "Acesso negado"')    

print('Sistema de login')
usuario_correto = "admin"
senha_correta = "1234"
usuario = input('Usuario: ')
senha = input('senha: ')
def sistema_login(usuario, senha):
    if usuario == usuario_correto and senha == senha_correta:
        print('Acesso permitido')
    else:
        print('Acesso negado')

sistema_login(usuario, senha)



print(' ')
print(f'1️⃣6️⃣ Média do aluno')
print('Peça 3 notas.')
print('Calcule a média.')
print('Se média >= 7 → "Aprovado"')
print('Senão → "Reprovado"')    

print('Média do Aluno')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
def calcula_media(n1, n2, n3):
    return(n1 + n2 + n3) / 3

media = calcaula_media(nota1, nota2, nota3)
if media >=7:
    print('Aprovado')
else:
    print('Reprovado')


print(' ')
print(f'1️⃣7️⃣ Menu Interativo')
print('Crie um menu:')
print('1 - Somar')
print('2 - Subtrair')
print('3 - Sair')
print('Use while para manter o programa rodando até escolher sair.')

def menu():
    while True:
        print('Menu: ')
        print('1 - Somar')
        print('2 - subtrair')
        print('3 - sair')
        escolha = input('Escolha uma opção: ')
        if escolha =='1':
            num1 = float(input('digite o primeiro numero:   '))
            num2 = float(input('digite o segundo numero: '))
            print(f'A soma é: {num1} + {num2} = {num1 + num2}')
        elif escolha == '2':
            num1 = float(input('digite o primeiro numero: '))
            num2 = float(input('digite o segundo numero: '))
            print(f'A subtração é: {num1} - {num2} = {num1 - num2}')
        elif escolha == '3':
            print('Saindo do programa. Até mais!')
            break
        else:
            print('Opção inválida. Tente novamente. ')
menu()
print(' ')
print(f'1️⃣8️⃣ Adivinhe o número')

print('Defina um número fixo (ex: 7).')
print('Peça ao usuário para tentar adivinhar.')
print('Use loop até acertar.')
numero_fixo = 3
while True:
    palpite = int(input('Tente advinhar o numero entre 1 e 10: '))
    if palpite == numero_fixo:
        print('Parabéns! voce acertou!')
        break
    else:
        print('Tente novamente. ')

print(' ')
print(f'1️⃣9️⃣ Contador de pares')
print('Peça um número N.')
print('Conte quantos números pares existem entre 1 e N.')
n = int(input('Diginte um número N: '))
contador_pares = 0
for i in range(1, n+1):
    if i % 2 ==0:
        contador_pares +=1
print(f'Entre 1 e {n} existem {contador_pares} números pares.')

print(' ')

print(f'2️⃣0️⃣ Mini Sistema Financeiro')
print('Peça:')
print('Salário')
print('Valor das despesas')
print('Calcule:')
print('Se sobrou dinheiro → mostrar valor restante')
print('Se ficou negativo → mostrar quanto faltou')

salario = float(input('Digite seu salário: R$ '))
despesas = float(input('Digite suas despesas: R$'))
saldo = salario - despesas
if saldo >0:
    print(f'Sobrou R$ {saldo:.2f} no seu saldo.')
elif saldo <0:
    print(f'Faltaram R$ {abs(saldo):.2f} no seu saldo.')
else:
    print('Seu saldo está zerado.')
