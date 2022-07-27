primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))
for c in range(1, 11):
    print(f'{c}° = {primeiroTermo + (c - 1) * razao}')
