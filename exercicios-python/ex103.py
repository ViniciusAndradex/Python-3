def ficha(jog='', gols=0):
    if jog == '':
        jog = '<desconhecido>'
    return f'O jogador {jog} fez {gols} gol(s) no campeonato.'


# Programa Principal
print('=' * 10)
jogador = str(input('Nome do Jogador: ')).strip()
gol = str(input('Número de Gols: ')).strip()
if gol == '' or gol.isalpha():
    gol = int(0)
else:
    gol = int(gol)
print(ficha(jogador, gol))
