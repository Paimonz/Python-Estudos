nome = str(input ('\033[33m\nDigite seu nome completo: \n\033[m'))
nomeM = nome.upper()
print ('\033[33m\nSeu nome completo com todas\nas letras maiúsculos é:\n\033[m',nomeM)
nomeMi = nome.lower()
print ('\033[33m\nSeu nome completo com todas\nas letras minúsculas é:\n\033[m',nomeMi)
nomeQ = nome.split()
p = nomeQ[0]
pr = len(p)
q = (''.join(nomeQ))
nomeq = len(q)
print (f'\033[33m\nSeu nome completo possui\033[32m {nomeq} \033[33m letras\033[m')
print(f'\033[33m\nSeu primeiro nome é \033[32m {p} \033[33me possui \033[32m{pr} \033[33mletras!\033[m')

