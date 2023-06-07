import datetime

nome =  'Lucas'
sobrenome = 'Corrêa dos Reis'
idade = 18
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
ano = date.strftime("%Y")
ano_nascimento = int(ano) - idade
maior_de_idade = idade >= 18
altura_em_m = 1.75


print('Nome:', nome)     
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade:', maior_de_idade)
print('Altura em metros:', altura_em_m)