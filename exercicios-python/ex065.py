media = num = maior = menor = cont = 0
resp = ''
while resp != 'N':
    num = int(input('Digite um número: '))
    if cont == 0:
        maior = menor = num
    else:
        if maior < num:
            maior = num
        elif menor > num:
            menor = num
    media += num
    cont += 1
    while resp != 'S' and resp != 'N':
        resp = str(input('Deseja Continuar [S/N]?\n-  ')).strip().upper()[0]
    if resp in 'S':
        resp = ''
    else:
        media /= cont
print()
print(f'Numeros digitados: {cont}\nMaior: {maior}\nMenor: {menor}\nMedia: {media:.2f}')
