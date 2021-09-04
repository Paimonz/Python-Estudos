a = float(input ('Digite a 1° nota do aluno: '))
b = float(input ('Digite a 2° nota do aluno: '))
m = (a + b) / 2

if m < 5:
    print ('Sua média foi de {}, REPROVADO!'.format(m))
elif m >= 7:
    print ('Você foi aprovado, sua média foi de {}'.format(m))
else:
    print ('Sua média foi de {}, RECUPERAÇÃO!'.format(m))
