f = str(input ('Digite uma frase:')).strip().lower()

d = f.split()
frase = ''.join(d)
print (frase)
n = len(frase)+1
print(n)

lista = [ ]

for c in range(0, n):
    lista.append(frase[n])
    n = n - 1
    
if frasse == lista:
    print('É um palíndromo!')
else:
    print ('A frase não é um palíndromo!)
