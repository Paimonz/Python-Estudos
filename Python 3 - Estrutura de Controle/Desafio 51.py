n = int(input('\nDigite o primeiro termo:'))
r = int(input ('Digite a razão da PA:'))
w = n + (10) * r
print ('\nA sequência de sua PA é:')
for c in range (n, w, r):
    print ('{}'.format(c),end='->')
print ('ACABOU')