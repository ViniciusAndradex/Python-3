matriz = [[], [], []]
par = terceiraC = 0
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin].append(int(input(f'Digite um valor para [{lin}, {col}]: ')))
        if matriz[lin][col] % 2 == 0:
            par += matriz[lin][col]
        if col == 2:
            terceiraC += matriz[lin][col]
print('=' * 10)
for p in matriz:
    for d in range(0, len(p)):
        print(f'[{p[d]:^5}]', end='')

    print()
print('=' * 10)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {terceiraC}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
