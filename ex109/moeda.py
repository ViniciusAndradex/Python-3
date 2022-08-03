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
