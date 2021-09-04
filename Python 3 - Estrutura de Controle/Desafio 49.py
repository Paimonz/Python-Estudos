t = int(input('\nDigite um número para ver sua tabuada:'))
n = 0
v = 0
print ('\n')
for c in range(1,11):
    n += 1
    v = t * n
    print (' {} x {} = {} '.format(t, n, v))