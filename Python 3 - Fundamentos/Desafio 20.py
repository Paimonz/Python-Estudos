from random import sample, shuffle
a1 = input ('\033[7m\nDigite o nome do primeiro aluno: ')
a2 = input ('Digite o nome do segundo aluno: ')
a3 = input ('Digite o nome do terceiro aluno: ')
a4 = input ('Digite o nome do quarto aluno: ')
lista = [a1, a2, a3,a4]
'''apresenta = sample(lista,k=len(lista))'''
print ('\033[m\nA sequência de apresentação será:')
shuffle(lista)
print ('\033[32m',(lista),'\033[m')