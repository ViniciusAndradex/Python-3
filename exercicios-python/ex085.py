num = [[], []]
for c in range(1, 8):
    x = int(input(f'Digite o {c}°. valor: '))
    if x % 2 == 0:
        num[0].append(x)
    else:
        num[1].append(x)
print(f'Os valores pares digitados foram: {sorted(num[0])}')
print(f'Os valores impares digitados foram: {sorted(num[1])}')
