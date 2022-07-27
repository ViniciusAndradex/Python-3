from datetime import date

media = 0
idadeVelho = 0
qtdMulher = 0
nomeVelho = ''
for c in range(1, 5):
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua data de nascimento: '))
    sexo = str(input('Sexo: ')).strip().upper()
    idade = date.today().year - idade
    media += idade
    if sexo[0] == 'M':
        if idadeVelho < idade:
            idadeVelho = idade
            nomeVelho = nome
    if sexo[0] == 'F' and idade < 20:
        qtdMulher += 1
    if c == 4:
        media = media / c
    print()
print(f'Media de Idade: {media}\nHomem mais velho: {idadeVelho}, {nomeVelho}\nMulheres menores de 20: {qtdMulher}')
