nome = 'Lucas'
peso = 110.0
altura = 1.80
imc = peso / (altura ** 2)


print('Olá', nome, 'seu IMC é:', imc)

if imc <= 18.5:
    print('Você está na classificação de Magreza')
elif 18.6 <= imc <= 24.9:
        print('Você está na classificação de Normal')

elif 25 <= imc <= 29.9:
        print('Você está na classificação de Sobrepeso')

elif 30 <= imc <= 39.9:
        print('Você está na classificação de Obesidade')

elif imc <= 40.0:
        print('Você está na classificação de Obesidade grave')

