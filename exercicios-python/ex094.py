livrodeouro = list()
pessoa = dict()
media = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip()
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
    pessoa['idade'] = int(input('Idade: '))
    media += pessoa['idade']
    livrodeouro.append(pessoa.copy())
    pessoa.clear()
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-*-' * 10)
media /= len(livrodeouro)
print(f'- O grupo tem {len(livrodeouro)} pessoas.')
print(f'- A média de idade é de {media:.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for li in livrodeouro:
    if li['sexo'] == 'F':
        print(li['nome'], end=' ')
print('\n- Lista das pessoas que estão acima da média: ')
for li in livrodeouro:
    if li['idade'] > media:
        print()
        for k, v in li.items():
            print(f'{k} = {v}', end='; ')
        print()
print('<<< ENCERRADO >>>')
