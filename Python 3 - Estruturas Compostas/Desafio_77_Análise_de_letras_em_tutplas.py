'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, 
você deve mostrar, para cada palavra, quais são as suas vogais.
                                                                Por Curso em Vídeo'''

Palavra = ('aprender', 'programar','linguagem','python',        #Criada tupla com algumas palavras
            'curso','gratis','estudar','praticar','trabalhar',
            'mercado', 'programador','futuro')

for p in Palavra:                                               #Para cada palavra dentro da tupla
    print(f'\nNa palavra {p.upper()} temos:', end = ' ')        #Mostra a palavra
    for letra in p:                                             #Para cada letra dentro da palavra
        if letra in 'aeiou':                                    #Verifica se contém as vogais aeiou
            print(letra, end = ' ')                             #Mostra as vogais que contém na palavra