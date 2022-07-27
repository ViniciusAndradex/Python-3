acumulador = 0
contador = 0
for c in range(1, 6 + 1):
    if c % 2 == 0:
        acumulador += c
        contador += 1
print(f'A soma dos {contador} números pares é {acumulador}')
