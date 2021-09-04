from datetime import date

ano = int(input ('Digite o ano de seu nascimento: '))
atual = date.today().year
idade = atual - ano

if idade <= 9:
    print ('\nSua categoria é \033[32mMIRIM\033[m')
elif idade <= 14:
    print ('\nSua categoria é \033[32mINFANTIL\033[m')
elif idade <= 19:
    print ('\nSua categoria é \033[32mJUNIOR\033[m')
elif idade <= 20:
    print ('\nSua categoria é \033[32mSÊNIO\033[m')
else:
    print ('\nSua categoria é \033[32mMASTER\033[m')