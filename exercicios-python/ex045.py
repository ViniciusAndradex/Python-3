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
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po')
sleep(1)
bot = randint(1, 3)
print('\033[1;35mPROCESSANDO...')
sleep(1)
print('-*-' * 6)
print(f'\033[1;32mVoce jogou {jogos[jogador]}\nO bot jogou {jogos[bot]}')
print('\033[1;35m-*-' * 6)
sleep(1)
if jogador == 1:
    if bot == 1:
        print('\033[1;33mDRAW')
    elif bot == 2:
        print(f'\033[1;36mYOU LOSE')
    elif bot == 3:
        print(f'\033[1;34mYOU WIN')
    else:
        print('INVALIDO')
elif jogador == 2:
    if bot == 1:
        print(f'\033[1;34mYOU WIN')
    elif bot == 2:
        print('\033[1;33mDRAW')
    elif bot == 3:
        print(f'\033[1;36mYOU LOSE')
    else:
        print('INVALIDO')
elif jogador == 3:
    if bot == 1:
        print(f'\033[1;36mYOU LOSE')
    elif bot == 2:
        print(f'\033[1;34mYOU WIN')
    elif bot == 3:
        print('\033[1;33mDRAW')
    else:
        print('INVALIDO')
else:
    print('OPÇÃO INVALIDA')
print('\033[1;35;40mTHANK YOU FOR PLAY MY GAME!\033[m')
