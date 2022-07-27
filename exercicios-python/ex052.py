primo = int(input('Digite um numero: '))
somaPrimo = 0
print('DIVISIVEIS ESTÃO COLORIDOS: ')
for c in range(1, primo + 1):
    if primo % c == 0:
        print(f'\033[1;34m{c}\033[m', end=' ')
        somaPrimo += 1
    else:
        print(f'{c}', end=' ')
print()
if somaPrimo != 2:
    print(f'\033[4;33m{primo}\033[m não é primo!')
else:
    print(f'\033[4;32m{primo}\033[m é primo!')
