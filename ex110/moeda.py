def metade(num):
    valor = moeda(num / 2)
    return valor


def dobro(num):
    valor = moeda(num * 2)
    return valor


def aumentar(num, perc):
    valor = moeda(num + (num * perc / 100))
    return valor


def diminuir(num, perc):
    valor = moeda(num - (num * perc / 100))
    return valor


def moeda(num):
    formatacao = f'R${num:.2f}'
    formatacao = formatacao.replace('.', ',')
    return formatacao


def resumo(num, aum, desc):
    print('-' * 32)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 32)
    print(f'{"Preço analisado:":22}{moeda(num)}')
    print(f'{"Dobro do preço:":22}{dobro(num)}')
    print(f'{"Metade do preço:":22}{metade(num)}')
    print(f'{f"{aum}% de aumento:":22}{aumentar(num, aum)}')
    print(f'{f"{desc}% de redução:":22}{diminuir(num, desc)}')
    print('-' * 32)
