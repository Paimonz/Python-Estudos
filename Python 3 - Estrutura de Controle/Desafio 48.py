
s = 0
for c in range(1,501):
    if c % 2 != 0 and c % 3 == 0:
        s += c
print ('''\nO valor total da soma no
intervalo de 1 a 500, considerando apenas
os números impares e múltiplos de 3
é: {}'''.format(s))