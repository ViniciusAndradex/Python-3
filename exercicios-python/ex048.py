soma = 0
for c in range(1, 500):
    if c % 3 == 0:
        for i in range(0, c+1):
            if 3 * i == c:
                soma += c
print(f'A soma dos multiplos de \033[4;33m{soma}')
