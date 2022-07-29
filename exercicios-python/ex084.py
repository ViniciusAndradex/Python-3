pessoas = list()
cadastro = list()
maior = menor = 0
while True:
    cadastro.append(str(input('Nome: ')))
    cadastro.append(float(input('Peso: ')))
    if maior == 0:
        menor = maior = cadastro[1]
    else:
        if maior < cadastro[1]:
            maior = cadastro[1]
        if menor > cadastro[1]:
            menor = cadastro[1]
    pessoas.append(cadastro[:])
    cadastro.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-' * 20)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
