from random import randint
from time import sleep


def sorteio(lis):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        lst = randint(1, 10)
        print(lst, end=' ')
        sleep(0.5)
        lis.append(lst)
    print('PRONTO!')


def somaPar(lst):
    soma = 0
    for c in lst:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lst}, temos {soma}')


# Programa Principal:
lista = list()
sorteio(lista)
somaPar(lista)
