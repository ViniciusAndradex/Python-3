nome = str(input('Digite seu nome: ')).strip()
if nome == 'vinicius':
    print('Que nome bonito, ')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia jessica Juliana':
    print('Belo nome feminino!')
else:#Opcional.
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia {nome}')
