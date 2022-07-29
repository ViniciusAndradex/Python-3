alunos = dict()
alunos['nome'] = str(input('Digite seu nome: '))
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))
if alunos['media'] >= 7.0:
    alunos['situacao'] = 'Aprovado'
elif alunos['media'] >= 5.0:
    alunos['situacao'] = 'Recuperação'
else:
    alunos['situacao'] = 'Reprovado'
print('-' * 15)
for k, v in alunos.items():
    print(f'- {k} é igual a {v}')
    