def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3


def leiaInt(msg):
    while True:
        try:
            x = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[1;31m{KeyboardInterrupt}: Usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return x


def leiaReal(msg):
    while True:
        try:
            x = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO: por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[1;31m{KeyboardInterrupt}: Usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return x
