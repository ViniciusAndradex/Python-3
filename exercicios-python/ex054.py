from datetime import date

maior = menor = 0
for c in range(1, 8):
    data = int(input('Digite seu ano de nascimento: '))
    if date.today().year - data >= 21:
        maior += 1
    else:
        menor += 1
print(f'Temos {maior} maiores de idade e {menor} menores de idade.')
