tupla = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
         int(input('Digite um número: ')))
print(f'Valores digitados: {tupla}')
print(f'Valor 9 foi digitado {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O número 3 apareceu na {tupla.index(3) + 1}° posição')
else:
    print('O número 3 não apareceu em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')
