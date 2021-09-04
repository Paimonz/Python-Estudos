from datetime import date

ano = int(input ('\nDigite o ano de seu nascimento:\n'))
atual = date.today().year
idade = atual - ano
alista = ano + 18

if idade < 18:
    print ('\nVocé ainda vai se alistar ao serviço militar')
    print ('Seu ano de alistamento militar será {}'.format(alista))
    f = 18 - idade
    print ('Ainda faltam {} anos para o seu alistamento'.format(f))
    
elif idade > 18:
    print ('\nVocê já passou do tempo do alistamento')
    f = idade - 18
    print ('Vocé está atrasado {} anos para o serviço militar'.format(f))
    print ('Seu ano de alistamento militar foi em {}'.format(alista))

else:
    print ('\Está na hora de se alistar!')
