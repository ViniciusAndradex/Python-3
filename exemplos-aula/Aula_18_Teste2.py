galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
print('-' * 15)
for p in galera:
    print(p)
    print(p[0])
    print(p[1])
print('-' * 15)
povo = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    povo.append(dado[:])
    dado.clear()
print(povo)
print('-' * 15)
maior = menor = 0
for p in povo:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade!')
        menor += 1
print(f'Menor: {menor}\nMaior: {maior}')
