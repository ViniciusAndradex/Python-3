sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Digite seu sexo[F/M]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
