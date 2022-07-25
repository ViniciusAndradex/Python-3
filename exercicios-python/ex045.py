from time import sleep
from random import randint

jogos = {1: 'Pedra',
         2: 'Papel',
         3: 'Tesoura'}
print('\033[1;35mVAMOS JOGAR JOKENPO')
jogador = int(input('''\033[1;34m[1] Pedra
[2] Papel
[3] Tesoura
\033[1;31m- '''))
bot = randint(1, 3)
print('\033[1;35mPROCESSANDO...')
sleep(2)
if jogador == 1:
    if bot == 1:
        print('\033[1;33mDRAW')
    elif bot == 2:
        print(f'\033[1;36mYOU LOSE, bot {jogos[bot]}')
    else:
        print(f'\033[1;34mYOU WIN, bot {jogos[bot]}')
elif jogador == 2:
    if bot == 1:
        print(f'\033[1;34mYOU WIN, bot {jogos[bot]}')
    elif bot == 2:
        print('\033[1;33mDRAW')
    else:
        print(f'\033[1;36mYOU LOSE, bot {jogos[bot]}')
elif jogador == 3:
    if bot == 1:
        print(f'\033[1;36mYOU LOSE, bot {jogos[bot]}')
    elif bot == 2:
        print(f'\033[1;34mYOU WIN, bot {jogos[bot]}')
    else:
        print('\033[1;33mDRAW')
print('\033[1;35;40mTHANK YOU FOR PLAY MY GAME!\033[m')
