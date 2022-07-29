pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('-' * 12)
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-' * 12)
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.6
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-' * 12)
del pessoas['sexo']
for k in pessoas.keys():
    print(k)
