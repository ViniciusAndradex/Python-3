tupla = ('Palmeiras', 'Corinthians', 'Fluminense', 'Atlético-MG', 'Athletico-PR', 'Flamengo', 'Internacional',
         'Bragantino', 'Santos', 'São Paulo', 'Botafogo', 'Ceará SC', 'Coritiba', 'Goiás', 'América-MG', 'Avaí',
         'Cuiabá', 'Atlético-GO', 'Juventude', 'Fortaleza')
print(f'{" BRASILEIRÃO ":=^31}')
print(f'TOP 5: {tupla[:5]}')
print(f'Z4: {tupla[:-5:-1]}')
print(f'Times na Ordem alfabética: {sorted(tupla)}')
print(f'Posição do Botafogo: {tupla.index("Botafogo") + 1}°')
