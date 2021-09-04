n = int(input('''
	\nDigite um progrma para ver 
o seu fatorial: '''))

cont = n
fatorial = 1


while cont > 0:
    resultado =  cont * (cont-1)
    fatorial *= cont
    cont-=1
    
    print ('{}'.format(resultado),end=' ')
    print ('x ' if cont > 0 else '= ', end ='')
print(fatorial)
