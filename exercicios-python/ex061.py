pa = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
while cont <= 10:
    print(f'{pa + (cont - 1) * razao}', end=' -> ')
    cont += 1
print('FIM')
