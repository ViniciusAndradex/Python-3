from random import randint
from time import sleep
sorteados = list()
sorteio = list()
numSorteio = int(input('Quantos jogos você quer que eu sorteie? '))
for num in range(0, numSorteio):
    cont = 0
    while True:
        x = randint(1, 60)
        if x not in sorteio:
            sorteio.append(x)
            cont += 1
        if cont >= 6:
            break
    sorteados.append(sorteio[:])
    sorteio.clear()
# Apresentação
print(f'{f" SORTEANDO {numSorteio} JOGOS ":-^40}')
for jogadas in range(0, numSorteio):
    print(f'Jogo {jogadas + 1:2}: {sorted(sorteados[jogadas])}')
    sleep(0.5)
print(f'{f" < BOA SORTE! > ":-^40}')
