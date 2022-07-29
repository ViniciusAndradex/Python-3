brasil = []
estado = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado)
brasil.append(estado1)
print(estado1)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
print('-' * 18)
estado2 = dict()
brasil1 = list()
for c in range(0, 3):
    estado2['uf'] = str(input('Unidade Federativa: '))
    estado2['sigla'] = str(input('Sigla '))
    brasil1.append(estado2.copy())
for e in brasil1:
    print(f'{e["sigla"]}: {e["uf"]}')
    for k, v in e.items():
        print(f'        {k}: {v}')

