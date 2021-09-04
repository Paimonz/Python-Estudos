n = input('\033[32;1m\nDigite algo: ')
print('\nO tipo primitivo desse valor é:\n\033[m', type(n))

print('\033[34m\nO valor é numérico?', n.isnumeric())
print('Só tem espaços?', n.isspace())
print('É alfabético?', n.isalpha())
print ('É alfanumérico?', n.isalnum())
print ('Está em maiúscula?', n.isupper())
print ('Está em minúscula?', n.islower())
print('Está capitalizada?', n.istitle())
print('\033[35m\n*#*#*# TESTANDO OUTRO MODO DE IMPRIMIR *#*#*#\033[m')
print (f'Só tem espaços? {n.isspace()}\033[m')

