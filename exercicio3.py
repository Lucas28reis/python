horas = input('Informe a hora em numeros inteiros: ')

# if int(horas) >= 0 and int(horas) <= 11:
#     print('Bom dia') 
# elif int(horas) >= 12 and int(horas) <= 17:
#     print('Boa Tarde') 
# elif int(horas) >= 18 and int(horas) <= 23:
#     print('Boa noite') 

try:
    hora = int(horas)

    if hora >= 0 and hora <= 11:
        print('Bom dia')

    elif hora >= 12 and hora <= 17:
        print('Boa Tarde') 
    
    elif hora >= 18 and hora <= 23:
        print('Boa noite') 

except:
    print('Digite apenas numeros inteiros')