lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print(lanche[::-1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print('-' * 20)
# Tuplas são imutaveis.
# Traceback: lanche[1] = 'Refrigerante'
print(len(lanche))

for cont in range(0, len(lanche)):
    print(f' 1 - Eu vou comer {lanche[cont]}, na posição {cont}')
for c in lanche:
    print(f'2 - Eu vou comer {c}')
for pos, c in enumerate(lanche):
    print(f'3 - Eu vou comer {c}, na posição {pos}')
print('-' * 20)
print(sorted(lanche))
