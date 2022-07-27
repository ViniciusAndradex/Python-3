maior = menor = 0
for c in range(1, 6):
    peso = float(input('Digite seu peso: '))
    if c == 1:
        maior = menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso
print(f'Mais pesado: {maior}Kg\nMais leve: {menor}Kg')
