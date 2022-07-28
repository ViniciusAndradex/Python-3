from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for c in tupla:
    print(c, end=' ')
print(f'\nMaior número: {max(tupla)}')
print(f'Menor número: {min(tupla)}')
