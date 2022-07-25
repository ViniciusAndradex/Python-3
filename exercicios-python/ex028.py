from random import randint

jogada = int(input('Adivinho o número do bot [0/5]: '))
bot = randint(0, 5)
if jogada == bot:
    print('Você venceu parabéns')
else:
    print(f'Você perdeu, o bot jogou {bot}')
