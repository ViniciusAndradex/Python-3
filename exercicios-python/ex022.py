nome = str(input('Digite seu nome completo: ')).strip()
print(f'MAIUSCULO: {nome.upper()}')
print(f'MINUSCULO: {nome.lower()}')
num = len(nome) - nome.count(' ')
print(f'Numero de letra: {len(nome) - nome.count(" ")}')
print(f'Numero de letras do primeiro nome: {len(nome.split()[0])}')
# ou print(f'Numero de letras do primeiro nome: {nome.find(" ")}')