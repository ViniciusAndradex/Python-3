km = float(input('Quantos km foram percorridos: '))
diasAlugados = int(input('Dias alugados: '))
print(f'Total a Pagar: R${(diasAlugados * 60) + (km * 0.15):.2f}')
