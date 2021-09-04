frase = str(input ('Digite uma frase:\n')).strip()
frase = frase.upper()
qtsA = frase.count('A')
pA = frase.find('A') + 1
uA = frase.rfind('A') + 1
print(f'\nNa sua frase existe {qtsA} letras As')
print(f'A primeira letra A aparece na posição {pA}!')
print (f'A última letra A aparecer na posição {uA}!')