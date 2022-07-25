from random import randint

jogada = int(input('Adivinho o número do bot [1/5]: '))
bot = randint(1, 5)
if jogada == bot:
    print('Você venceu parabéns')
else:
    print(f'Você perdeu, o bot jogou {bot}')