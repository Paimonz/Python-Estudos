ca = float(input('\033[1;7mDigite o valor do cateto adjacente\033[m: '))
co = float(input ('\033[1;7mDigite o valor do cateto oposto\033[m:'))
a = ca**2
o = co**2
h = (a + o)**(1/2)
print (f'\033[41mO valor da hipotenusa é: {h}\033[m')