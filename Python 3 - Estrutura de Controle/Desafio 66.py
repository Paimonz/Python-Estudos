print('\nSomador de números [ Digite 999 para parar!]')
soma =  cont = 0
print('\n')

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    cont += 1

print(f'A quantidade de número digitado foi de {cont} e a soma entre eles {soma}')