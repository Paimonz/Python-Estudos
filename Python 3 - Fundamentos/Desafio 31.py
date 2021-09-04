v = int(input ('\nQual a distância da viagem em KM?: '))
if v >= 200:
    pv = 0.5 * v
    print (f'O preço para essa viagem será de {pv}')
else:
    pv = 0.45 * v
    print (f'O preço para essa viagem será de R$:{pv}')