from random import choice
a1 = input ('\033[42mDigite o nome do primeiro aluno: ')
a2 = input ('\033[43mDigite o nome do segundo aluno: ')
a3 = input ('\033[44mDigite o nome do terceiro aluno: ')
a4 = input ('\033[45mDigite o nome do quarto aluno: ')
lista = [a1, a2, a3,a4]
sorteio = choice(lista)
print ('\033[7m\n O aluno escolhido foi:{}{}{} '.format('\033[32m',sorteio, '\033[m'))