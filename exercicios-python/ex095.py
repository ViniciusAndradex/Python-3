aproveitamento = dict()
tabela = list()
ngols = list()
while True:
    aproveitamento['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
    njogos = int(input(f'Quantas partidas {aproveitamento["nome"]} jogou?\n- '))
    for c in range(0, njogos):
        ngols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    aproveitamento['gols'] = ngols[:]
    aproveitamento['total'] = sum(ngols)
    tabela.append(aproveitamento.copy())
    ngols.clear()
    aproveitamento.clear()
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
    print('-*-' * 30)
    if resp == 'N':
        break
print(f'cod {"nome":15}{"gols":15}{"Total":15}')
print('-' * 43)
for pos, v in enumerate(tabela):
    print(f'{pos:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 43)
while True:
    while True:
        opc = int(input('Mostrar dados de qual jogador? (999 para parar) '))
        if opc >= len(tabela) and opc != 999:
            print(f'ERRO! NÃO EXISTE JOADOR COM CÓDIGO {opc}! TENTE NOVAMENTE')
            print('-' * 43)
        else:
            break
    if opc == 999:
        print('<<< VOLTE SEMPRE >>>')
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {tabela[opc]["nome"]}')
    for pos, val in enumerate(tabela[opc]['gols']):
        print(f'    No jogo {pos + 1} fez {val} gols.')
    print('-' * 43)
