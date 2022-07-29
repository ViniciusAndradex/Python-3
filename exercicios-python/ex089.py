from time import sleep
doc = list()
alunos = list()
notas = list()
while True:
    alunos.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    alunos.append(notas[:])
    alunos.append((notas[0] + notas[1]) / 2.0)
    doc.append(alunos[:])
    alunos.clear()
    notas.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-=' * 15)
print(f'{"No.":4}{"NOME":15}{"MÉDIA":5}')
print('-' * 30)
for pos, li in enumerate(doc):
    print(f'{pos:<4}{li[0]:16}{li[2]:.1f}')
print('-=' * 15)
sleep(1)
while True:
    while True:
        mostrarNota = int(input('Mostrar notas de qual aluno? [999 Interrompe]: '))
        if 0 <= mostrarNota <= 3 or mostrarNota == 999:
            break
    if mostrarNota == 999:
        print('FINALIZANDO...')
        sleep(1)
        break
    print(f'Notas de {doc[mostrarNota][0]} são {doc[mostrarNota][1]}')
    print('-=' * 15)
    sleep(1)
print('<<< VOLTE SEMPRE >>>')
