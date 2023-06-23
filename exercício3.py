nome = input('Digite o seu nome: ')

if len(nome) <= 4  and len(nome) > 1:
    print('Seu nome é curto')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal')
elif len(nome) > 6:
    print('Seu nome é muito grande')

else:
    print('Digite um nome')


