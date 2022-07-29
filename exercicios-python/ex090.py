alunos = dict()
alunos['nome'] = str(input('Digite seu nome: '))
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))
print('-' * 15)
print(f'- nome é igual a {alunos["nome"]}')
print(f'- média é igual a {alunos["media"]}')
if alunos['media'] >= 7.0:
    alunos['situacao'] = 'Aprovado'
elif alunos['media'] >= 5.0:
    alunos['situacao'] = 'Recuperação'
else:
    alunos['situacao'] = 'Reprovado'
print(f'- situação é igual a {alunos["situacao"]}')
