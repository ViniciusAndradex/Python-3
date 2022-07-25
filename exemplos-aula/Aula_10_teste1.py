nome = str(input('Qual seu nome: '))
if nome == 'Pio':
    print('Que nome lindo você tem, ', end='')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2.0
print(f'Sua média foi {m:.1f}')
if m >= 6.0:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua nota foi péssima!')
