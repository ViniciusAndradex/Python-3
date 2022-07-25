from datetime import date

ano = int(input('Digite um ano qualquer (0 para calcular o ano da minha máquina): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'ANO BISSEXTO (\033[1;36m{ano}\033[m)')
else:
    print(f'\033[1;35;42m{ano}\033[m NÃO É BISSEXTO')
