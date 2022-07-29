matriz = [[], [], []]
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin].append(int(input(f'Digite um valor para [{lin}, {col}]: ')))
print('-' * 14)
for p in matriz:
    for d in range(0, len(p)):
        print(f'[{p[d]:^5}]', end='')
    print()
