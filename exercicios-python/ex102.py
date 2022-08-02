def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O Número a ser calculado.
    :param show: (OPCIONAL) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    if not show:
        for c in range(num, 0, -1):
            f *= c
        return f
    else:
        for c in range(num, 0, -1):
            print(f'{c}', end='')
            if c != 1:
                print(end=' x ')
            else:
                print(end=' = ')
            f *= c
        return f


# Programa Princiapal
print(fatorial(4))
print(fatorial(4, show=True))
help(fatorial)
