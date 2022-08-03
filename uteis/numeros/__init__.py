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
            x = int(x)
            return x
        except Exception as erro:
            print(f'\033[1;31m{erro.}: por favor, digite um número inteiro válido.\033[m')
