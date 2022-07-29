valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for c in valores:
    print(f'{c}...', end=' ')
print('-' * 25)
for pos, v in enumerate(valores):
    print(f'na posição {pos} encontrei o valor {v}...')
print('Cheguei ao final da lista.')
print('-' * 25)
lista = list()
for c in range(0, 5):
    lista.append(int(input('Digite um numero: ')))
for pos, v in enumerate(lista):
    print(f'na posição {pos} encontrei o valor {v}...')
print('Cheguei ao final da lista.')
print('-' * 25)
a = [2, 3, 4, 7]
# b = a ligando listas
b = a[:] # Copiando a para b
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
