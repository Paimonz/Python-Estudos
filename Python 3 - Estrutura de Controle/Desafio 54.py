from datetime import date
hoje = date.today().year

print (hoje)
contMaior = 0
contMenor = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}° pessoa:'.format(c)))
    maior = hoje - ano
    if maior >= 21:
        contMaior += 1
    else:
        contMenor += 1
print('{} pessoas são maiores de idade e {} pessoas são menores de idade'.format(contMaior, contMenor))