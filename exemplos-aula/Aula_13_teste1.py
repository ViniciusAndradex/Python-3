print('-' * 15)
for c in range(1, 7):
    print(c)
print('FIM')
print('-' * 15)
for c in range(6, 0, -1):
    print(c)
print('Fim')
print('-' * 15)
ini = int(input('Digite um numero: '))
fim = int(input('Digite um numero: '))
passo = int(input('Digite um numero: '))
for c in range(ini, fim + 1, passo):
    print(c)
print('-' * 15)
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print(f'Soma: {s}')
print('-' * 15)
