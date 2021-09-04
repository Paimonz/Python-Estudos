print ('\n')
print ('_-_'*15)
print (' '*15 + 'LOJAS DIAS' + ' '*15)
print ('_-_'*15)

v = float (input ('\nDigite o valor da sua compra RS:\n'))
print ('\n	[ 1 ] à vista dinheiro/cheque')
print (' [ 2 ] à vista no cartão')
print ('	[ 3 ] 2x no cartão')
print ('	[ 4 ] 3x ou mais')

p = int(input('\nQual será a forma de pagamento?\n'))


if p == 1:
    vp = v -(( 10 / 100) * v) 
    print ('A sua compra de R$:{:.0f} irá sair por R$:{:.0f}'.format(v,vp))
elif p == 2:
    vp = v - ((5/100)*v)
    print ('A sua compra de R$:{:.0f} irá sair por R$:{:.0f}'.format(v,vp))  
elif p == 3:
    parcela = v / 2
    print ('Sua compra será parcelada em 2x de {:.2f}'.format(parcela))
    print ('A sua compra de R$:{:.0f} irá sair por R$:{:.0f}'.format(v,v))
elif p == 4:
    q = int(input ('Em quantas vezes deseja parcelar?'))
    vp = ((20/100)*v) + v
    qp = vp/q
    print ('Sua compra ficou em {}x de R$:{:.2f}'.format(q,qp))
    print ('A sua compra de R$:{:.0f} irá sair por R$:{:.0f}'.format(v,vp))
else:
    print ('\nOpção Invalida!')