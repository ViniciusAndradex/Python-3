def metade(num, show=False):
    valor = num / 2
    if show:
        valor = moeda(valor)
    return valor


def dobro(num, show=False):
    valor = num * 2
    if show:
        valor = moeda(valor)
    return valor


def aumentar(num, perc, show=False):
    valor = num + (num * perc / 100)
    if show:
        valor = moeda(valor)
    return valor


def diminuir(num, perc, show=False):
    valor = num - (num * perc / 100)
    if show:
        valor = moeda(valor)
    return valor


def moeda(num):
    formatacao = f'R${num:.2f}'
    formatacao = formatacao.replace('.', ',')
    return formatacao


def resumo(num, aum=10, desc=10):
    print('-' * 32)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 32)
    print(f'{"Preço analisado:":22}{moeda(num)}')
    print(f'{"Dobro do preço:":22}{dobro(num, True)}')
    print(f'{"Metade do preço:":22}{metade(num, True)}')
    print(f'{f"{aum}% de aumento:":22}{aumentar(num, aum, True)}')
    print(f'{f"{desc}% de redução:":22}{diminuir(num, desc, True)}')
    print('-' * 32)
