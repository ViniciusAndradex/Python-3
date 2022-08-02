from time import sleep


def lin():
    print('-*-' * 15)


def contadorc():
    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(1, 11):
        print(c, end=' ')
        sleep(0.7)
    print('Fim!')


def contadord():
    print('Contagem de 10 até 0 de 2 em 2')
    for c in range(10, -1, -2):
        print(c, end=' ')
        sleep(0.7)
    print('Fim!')


def contador(inicio, fim, passo):
    if inicio > fim:
        if passo == 0:
            passo = -1
        elif passo > 0:
            passo = -passo
    elif inicio < fim:
        if passo == 0:
            passo = 1
        elif passo < 0:
            passo = abs(passo)
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    for c in range(inicio, fim - 1, passo):
        print(c, end=' ')
        sleep(0.5)
    print('FIM!')


# Programa Principal
lin()
contadorc()
lin()
contadord()
lin()
print('Agora é sua vez de personalizar a contagem!')
contador(inicio=int(input('Início: ')), fim=int(input('Fim: ')), passo=int(input('Passo: ')))
lin()
