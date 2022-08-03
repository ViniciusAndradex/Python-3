def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3


def leiaInt(num):
    while True:
        try:
            x = int(input(num))
            return x
        except ValueError:
            print(f'\033[1;31m{ValueError}: por favor, digite um número inteiro válido.\033[m')

def leiaReal(num):
    while True:
        try:
            x = float(input(num))
            return x
        except ValueError:
            print(f'\033[1;31m{ValueError}: por favor, digite um número real válido.\033[m')
