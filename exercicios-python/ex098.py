from time import sleep


def lin():
    print('-*-' * 15)


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
    if fim <= 0:
        fim -= 1
    else:
        fim += 1
    for c in range(inicio, fim, passo):
        print(c, end=' ')
        sleep(0.5)
    print('FIM!')


# Programa Principal
lin()
contador(1, 10, 1)
lin()
contador(10, 0, 2)
lin()
print('Agora é sua vez de personalizar a contagem!')
contador(inicio=int(input('Início: ')), fim=int(input('Fim: ')), passo=int(input('Passo: ')))
lin()
