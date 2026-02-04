#Calculando idade com Python a partir de input
nome = input("Qual o seu nome?")
print("Prazer em te conhecer! " + nome)
ano_nascimento = input("Em que ano você nasceu?")
ano_atual = 2026
idade = ano_atual - int(ano_nascimento)
print("Olá " + nome + ", você tem " + str(idade) + " anos de idade.")
