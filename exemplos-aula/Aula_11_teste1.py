#dicionario de cores
cores = {'limpa': '\033[m',
         'sublinhadoazul': '\033[4;34m'}
print('\033[1;30;41mteste\033[m')
print('\033[4;33;44mteste\033[m')
print('\033[1;35;43mteste\033[m')
print('\033[0;97;42mteste\033[m')
print('\033[mteste\033[m')
print('\033[7;97mteste\033[m')
print(f'{cores["sublinhadoazul"]}teste{cores["limpa"]}')
