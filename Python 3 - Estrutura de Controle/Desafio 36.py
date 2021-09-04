from time import sleep
print ('\n')
print ('*_*'*15)
print( '\033[32m          ANALISANDO SEU EMPRÉSTIMO\033[m')
print ('*_*'*15)

casa = float(input ('\nDigite o valor da casa que deseja comprar\nR$:'))
salário = float (input ('\nDigite o valor do seh salário\nR$:'))
ano = int(input ('\nDigite em quantos anos irá pagar a casa:\n'))

vp = casa / (ano * 12)
s3 = (30/100) * salário

print ('\033[31mPROCESSANDO...\033[m')
sleep(3)
if vp > s3:
    print ('\bnEmprestimo negado, pois o valor da parcela é maior que 30% do seu salário!')
else:
    print ('Empréstimo liberado!')
print ('Para pagar essa casa em {} anos o valor mensal será de R$: {:.2f}'.format(ano,vp)) 
