ano = int(input('Digite um ano qualquer: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'ANO BISSEXTO ({ano})')
else:
    print(f'{ano} NÃO É BISSEXTO')
