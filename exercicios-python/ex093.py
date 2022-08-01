aproveitamento = dict()
aproveitamento['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
njogos = int(input(f'Quantas partidas {aproveitamento["nome"]} jogou?\n- '))
ngols = list()
for c in range(0, njogos):
    ngols.append(int(input(f'Quantos gols na partida {c}? ')))
aproveitamento['gols'] = ngols[:]
aproveitamento['total'] = sum(ngols)
print('-' * 35)
print(aproveitamento)
print('-' * 35)
for k, v in aproveitamento.items():
    print(f'O campo {k} tem o valor {v}.')
print('-' * 35)
print(f'O jogador {aproveitamento["nome"]} jogou {len(aproveitamento["gols"])} partidas.')
for pos, val in enumerate(aproveitamento['gols']):
    print(f'    => Na partida {pos}, fez {val} gols.')
print(f'Foi um total de {aproveitamento["total"]}')
