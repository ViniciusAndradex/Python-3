def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


def soma(a=0, b=0, c=0):
    """
    Faz a soma entre os Parâmetros
    :param a: Valor Inteiro
    :param b: Valor Inteiro
    :param c: Valor Inteiro
    :return: Sem Retorno
    :author: Vinicius Andrade
    """
    s = a + b + c
    print(s)


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


soma(1, b=4)
help(soma)
print('-' * 10)
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}')
print('-' * 10)
print(par(9))
