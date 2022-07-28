qtdMaiores = qtdHomens = qtdMulheresMenor18 = 0
print('-' * 30)
while True:
    idade = int(input('Digite sua idade: '))
    while True:
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
        if sexo in 'FM':
            break
    print('-' * 30)
    if idade >= 18:
        qtdMaiores += 1
    if sexo in 'M':
        qtdHomens += 1
    if sexo in 'F' and idade < 20:
        qtdMulheresMenor18 += 1
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if resp in 'SN':
            print('-' * 30)
            break
    if resp in 'N':
        print(f'{" FIM DO PROGRAMA ":=^30}')
        break
print(f'Pessoa com mais de 18: \033[1;32m{qtdMaiores}\033[m')
print(f'Total de homens: \033[1;34m{qtdHomens}\033[m')
print(f'Total de mulher menores de 20 anos: \033[1;36m{qtdMulheresMenor18}\033[m')
