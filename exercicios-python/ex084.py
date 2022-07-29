pessoas = list()
cadastro = list()
while True:
    cadastro.append(str(input('Nome: ')))
    cadastro.append(float(input('Peso: ')))
    pessoas.append(cadastro[:])
    cadastro.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print(f'Ao todo, você cadastrou {len(pessoas)}')
maior = menor = 0
for p in pessoas:
    if maior == 0:
        menor = maior = p[1]
    else:
        if maior < p[1]:
            maior = p[1]
        if menor > p[1]:
            menor = p[1]
print('-' * 20)
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
