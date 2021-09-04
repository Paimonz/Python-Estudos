from time import sleep
v = int(input ('\nDigite a velocidade do carro: '))
if v > 80:
    print ('\nVocê foi multado!')
    print ('Calculando sua multa...')
    sleep(5)
    m = (v - 80) * 7
    print (f'Sua multa será de R$:{m}')
else:
    print ('Tenha uma boa viagem!')