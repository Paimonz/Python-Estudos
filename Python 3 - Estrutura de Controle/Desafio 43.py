p = float (input ('Digite seu peso Kg: '))
a = float(input ('Digite sua altura: '))

imc = p/a**2

#print (imc)

if imc < 18.5:
    print ('Você está abaixo do peso!')
elif imc <= 25:
    print ('Você está com o peso ideal!')
elif imc <= 30:
    print('Você está com SOBREPESO!')
elif imc <= 40:
    print('Você está com OBESIDADE!')
else:
    print ('Obesidade Mórbida!')