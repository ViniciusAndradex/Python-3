pa = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = 1
cont = 10
num = 0
while termo != 0:
    print(f'{pa + (termo - 1) * razao}', end=' -> ')
    termo += 1
    if termo == cont:
        print('PAUSA')
        cont = int(input('\nDeseja exibir mais quantos termo (0 para sair)?\n - '))
        if cont == 0:
            termo = cont
        else:
            cont += termo
            num = cont
print(f'Foram mostrados {num} termos.')
