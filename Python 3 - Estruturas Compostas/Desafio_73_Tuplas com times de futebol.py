'''Crie uma tupla preenchida com os 20 primeiros colocados da tabala do Campeonato Brasileiro de Futebol, na ordem
de colocação.Depois Mostre:

a) Os 5 primeiros
b) Os últimos 4 colocados
c)Time em ordem alfabética.
d)Em que posição está o time da Chapecoense.
                                                    por Curso em Vídeo'''

times = ('Atlético-MG','Palmeiras','Fortaleza','Bragantino','Flamengo','Corinthians','Fluminense',
        'Atlético-GO','Atlético-PR','Ceará SC','Cuiabá','Internacional','Juventude','Santos','São Paulo',
        'Bahia','América-MG','Sport Recife','Grêmio','Chapecoense') #Tupla criada com os times do Brasileirão (08/09/2021).

print('\nOs 5 primeiros  times da tabela do Campeonato Brasileiros são:')
print(times[:5])    #Fatiamente para pegar os 5 primeiros elementos.
print('\n')

print('Os últimos 4 colocados da tabela do Campeonato Brasileiro são:')
print(times[-4:])   #Fatiamento para pegar os 4 últimos elementos.
print('\n')

print('Os times da tabela do Campeonato Brasileiro organizados em ordem alfabética ficam:')
print(sorted(times))    #Sorted organiza a tupla em ordem alfábética.
print('\n')

print(f'O Chapecoense está na posição {times.index("Chapecoense")+1}°') #Para encontra a posição de "x" elemento 
print('\n')                                                             #basta utilizar .index, como a contagem das
                                                                        #  tuplas começam em 0 foi necessário 
                                                                        # acrescentar "+1" para representar 
                                                                        #adequadamento a posição do elemento.
