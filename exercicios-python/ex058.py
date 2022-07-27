from random import randint
from time import sleep
bot = randint(0, 10)
jogador = ''
cont = 0
while jogador != bot:
    jogador = int(input('Descubra o número sorteado pelo bot [0 / 10]: '))
    cont += 1
    print('Processando...')
    sleep(0.5)
    if jogador != bot:
        if jogador > bot:
            print('\033[1;31mMenor\033[m')
        else:
            print('\033[1;33mMaior\033[m')
        print('Tente novamente...')
print(f'Parabéns você conseguiu acertar em \033[1;35m{cont}\033[m vezes')
print(f'O número jogado foi \033[1;34m{jogador}')
