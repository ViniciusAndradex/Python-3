maior = menor = 0
for c in range(1, 6):
    peso = float(input('Digite seu peso: '))
    if c == 1:
        maior = menor = peso
    elif maior < peso:
        maior = peso
    elif menor > peso:
        menor = peso
print(f'Mais pesado: {maior}\nMais leve: {menor}')
