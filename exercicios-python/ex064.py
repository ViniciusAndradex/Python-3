soma = cont = n = 0
while n != 999:
    n = int(input('Digite um número (999 - encerra): '))
    if n != 999:
        cont += 1
        soma += n
print(f'Total de número digitados {cont}, somando {soma}')
