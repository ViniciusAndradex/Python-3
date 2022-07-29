from random import randint
from time import sleep
sorteados = list()
sorteio = list()
numSorteio = int(input('Quantos jogos você quer que eu sorteie? '))
for num in range(0, numSorteio):
    for jogos in range(0, 6):
        sorteio.append(randint(1, 60))
    sorteados.append(sorteio[:])
    sorteio.clear()
# Apresentação
print(f'{f" SORTEANDO {numSorteio} JOGOS ":-^40}')
for jogadas in range(0, numSorteio):
    print(f'Jogo {jogadas + 1}: {sorteados[jogadas]}')
    sleep(0.5)
print(f'{f" < BOA SORTE! > ":-^40}')
