def metade(num):
    return num / 2


def dobro(num):
    return num * 2


def aumentar(num, perc):
    return num + (num * perc / 100)


def diminuir(num, perc):
    return num - (num * perc / 100)


def moeda(num):
    formatacao = f'R${num:.2f}'
    formatacao = formatacao.replace('.', ',')
    return formatacao
