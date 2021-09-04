c = input('\nDigite o nome da sua cidade:\n ')
cidade = c.upper()
cidade = cidade.split()
s = (cidade[0])
if 'SANTO' == s:
    print ('Sua cidade começa com a palavra Santo')
else:
    print ('Sua cidade não começa com a palavra Santo')