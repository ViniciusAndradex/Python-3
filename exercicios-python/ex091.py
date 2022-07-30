from random import randint
from time import sleep
from operator import itemgetter
jogadas = dict()
ranking = dict()
print('Valores sorteados: ')
for c in range(1, 5):
    jogadas[f'jogador{c}'] = randint(1, 6)
for k, v in jogadas.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-' * 36)
print(f'  {"== RANKING DOS JOGADORES ==":26}')
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'   {i + 1} lugar: {v[0]} com {v[1]}')
    sleep(1)
