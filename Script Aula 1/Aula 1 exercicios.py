"""
Lista de Exercícios: Strings em Python
Contador de Caracteres: Peça ao usuário para digitar uma frase e imprima quantos caracteres ela possui (incluindo espaços).

Grito no Terminal: Receba um nome e exiba-o totalmente em letras maiúsculas.

Busca de Letra: Peça uma frase e, em seguida, uma letra. O programa deve dizer quantas vezes essa letra aparece na frase.

Primeiro e Último: Dada uma palavra digitada pelo usuário, exiba apenas a primeira e a última letra dela.

Inversor de Nomes: Peça o nome do usuário e o imprima de trás para frente (ex: "Python" vira "nohtyP").

Substituição de Censores: Peça uma frase e peça para o usuário escolher uma palavra para "esconder". Substitua todas as ocorrências dessa palavra por asteriscos (****).

Verificador de Domínio: Peça um e-mail e verifique se ele termina com @gmail.com. Retorne True ou False.

Formatação de Título: Peça o nome completo de uma pessoa em letras minúsculas e transforme-o para o formato de título (onde a primeira letra de cada nome é maiúscula).

Remover Espaços: Peça uma frase que contenha espaços extras no início e no fim (ex: " olá ") e exiba a frase "limpa", sem esses espaços.

Detector de Vogais: Peça uma palavra e conte quantas vogais (a, e, i, o, u) ela possui.
"""


#Contador de Caracteres: Peça ao usuário para digitar uma frase e imprima quantos caracteres ela possui (incluindo espaços).
frase = input("Olá usuário, este é o primeiro exercicio, digite uma frase: ")
print(f"a frase possui {len(frase)} caracteres.")

#Grito no Terminal: Receba um nome e exiba-o totalmente em letras maiúsculas.
nome = input("Digite seu nome: ")
print(nome.upper())

#Busca de Letra: Peça uma frase e, em seguida, uma letra. O programa deve dizer quantas vezes essa letra aparece na frase.
frase2 = input("Digite uma frase: ")
letra = input("Digite uma letra para saber quantas vezes ela aparece na frase: ")   
print(f"A letra '{letra}' aparece {frase2.count(letra)} vezes na frase.")

#Primeiro e Último: Dada uma palavra digitada pelo usuário, exiba apenas a primeira e a última letra dela.
palavra = input("Digite uma palavra: ") 
print(f"A primeira letra é '{palavra[0]}' e a última letra é '{palavra[-1]}'.")

#Inversor de Nomes: Peça o nome do usuário e o imprima de trás para frente (ex: "Python" vira "nohtyP").
nome2 = input("Digite seu nome: ")
print(f"Seu nome de trás para frente é: {nome2[::-1]}")

#Substituição de Censores: Peça uma frase e peça para o usuário escolher uma palavra para "esconder". Substitua todas as ocorrências dessa palavra por asteriscos (****).
frase3 = input("Digite uma frase: ")
palavra_censurada = input("Digite uma palavra que você quer censurar na frase: ")
frase_censurada = frase3.replace(palavra_censurada, "****")
print(frase_censurada)  

#Verificador de Domínio: Peça um e-mail e verifique se ele termina com @gmail.com. Retorne True ou False.
email = input("Digite seu e-mail: ")
print(email.endswith("@gmail.com")) 

#Formatação de Título: Peça o nome completo de uma pessoa em letras minúsculas e transforme-o para o formato de título (onde a primeira letra de cada nome é maiúscula).
nome_completo = input("Digite seu nome completo em letras minúsculas: ")    
print(nome_completo.title())    

#Remover Espaços: Peça uma frase que contenha espaços extras no início e no fim (ex: " olá ") e exiba a frase "limpa", sem esses espaços.
frase4 = input("Digite uma frase com espaços extras no início e no fim: ")
print(f"Sua frase sem espaços extras é: '{frase4.strip()}'")

#Detector de Vogais: Peça uma palavra e conte quantas vogais (a, e, i, o, u) ela possui.
palavra2 = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"
contador_vogais = sum(1 for letra in palavra2 if letra in vogais)   
print(f"A palavra '{palavra2}' possui {contador_vogais} vogais.")
    
