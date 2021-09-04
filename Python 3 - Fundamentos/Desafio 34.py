s = float (input ('\nQual o seu salário?\nR$:'))
if s > 1250:
    ns = ((10 / 100)*s) + s
    print ('Seu salário de R$:{:.2f} com aumento de 10% vai para R$:{:.2f}'.format(s, ns))
else:
    ns = ((15/ 100)*s) + s
    print ('Seu salário de R$:{:.2f} com aumento de 15% vai para R$:{:.2f}'.format(s, ns))