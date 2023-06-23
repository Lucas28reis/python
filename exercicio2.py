numero = input('Digite um número inteiro: ')

if numero.isdigit():

    num = int(numero)
    resto = num % 2

    if resto == 0:
        print('Este número é par')
        
    else:
        print('Este número é impar')

else:
    print(f'O número {numero} não é inteiro. Digite um número inteiro')
