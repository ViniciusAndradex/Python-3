val = list()
while True:
    num = int(input('Digite um valor: '))
    if num in val:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        val.append(num)
    while True:
        resp = str(input('Deseja Continuar [S/N]?\n')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
val.sort()
print(f'Você digitou os valores {val}')
