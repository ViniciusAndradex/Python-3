c = 1
while c < 10:
    print(c)
    c += 1
print('-*-' * 5)
c = 1
while c != 0:
    c = int(input('Digite um valor: '))
print('Fim')
print('-*-' * 5)
r = 'S'
while r == 'S':
    c = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? '))
print('Fim')
print('-*-' * 5)
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'{par} par\n{impar} impar.')
