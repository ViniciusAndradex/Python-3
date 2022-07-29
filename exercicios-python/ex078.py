lista = list()
for c in range(0, 5):
    lista.append(int(input(f'Digite um número Posição {c}: ')))
print(f'Valores da lista: {lista}')
print(f'O maior valor digitado foi {max(lista)} na posições ', end='')
for pos, lis in enumerate(lista):
    if lis == max(lista):
        print(pos, end='... ')
print(f'\nO menor valor digitado foi {min(lista)} na posições ', end='')
for pos, li in enumerate(lista):
    if li == min(lista):
        print(pos, end='... ')
