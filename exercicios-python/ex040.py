n1 = float(input('Digite a n1: '))
n2 = float(input('Digite a n2: '))
media = (n1 + n2) / 2.0
print(f'MEDIA: {media:.1f}')
if media < 5.0:
    print('\033[1;31mSTATUS: REPROVADO')
elif media <= 6.9:
    print('\033[1;33mSTATUS: RECUPERAÇÃO')
else:
    print('\033[1;34mSTATUS: APROVADO\033[m')
