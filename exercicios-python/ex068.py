from random import randrange
from time import sleep
win = 0
print('=-' * 30)
while True:
    print(f'{"VAMOS JOGAR PAR OU IMPAR":^58}')
    print('=-' * 30)
    bot = randrange(0, 11)
    jogada = ''
    while True:
        jogada = str(input('PAR OU IMPAR [P/I]: ')).strip().upper()[0]
        if jogada in 'PI':
            break
    num = int(input('Digite um número: '))
    soma = bot + num
    print('\033[1;36mPROCESSANDO...\033[m')
    sleep(0.5)
    print('-' * 30)
    print(f'Você jogou {num} e o bot {bot}.', end=' ')
    if soma % 2 == 0:
        print(f'Total de {soma} DEU PAR')
        print('-' * 30)
        sleep(0.5)
        if jogada in 'P':
            print('Você VENCEU!\nVamos jogar novamente...')
            win += 1
            print('-' * 30)
        else:
            print('Você PERDEU!')
            break
    else:
        print(f'Total de {soma} DEU IMPAR')
        print('-' * 30)
        sleep(0.5)
        if jogada in 'I':
            print('Você VENCEU!\nVamos jogar novamente...')
            win += 1
            print('-' * 30)
        else:
            print('Você PERDEU!')
            break
print('=-' * 30)
if win == 1:
    print(f'GAME OVER! Você venceu {win} vez.')
else:
    print(f'GAME OVER! Você venceu {win} vezes.')
