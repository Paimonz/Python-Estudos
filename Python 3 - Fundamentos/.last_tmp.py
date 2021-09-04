print ('\n')
print (' Somador de número! [ Digite 999 para parar!]')

soma = cont = 0


while True:
    if n == 999:
        break
    n = int(input ('\nDigite o número: '))
    soma += n
    cont += 1
    
print (f'Você digitou {cont} números e a soma entre eles é de: {soma}')