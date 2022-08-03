def nota(* notas, situacao=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias notas).
    :param situacao: valor opcional, indicando sobre a situação da turma.
    :return: dicinário com várias informações sobre a situação da turma.
    """
    media = 0
    aluno = dict()
    aluno['total'] = len(notas)
    aluno['maior'] = max(notas)
    aluno['menor'] = min(notas)
    for c in notas:
        media += c
    aluno['media'] = media / aluno['total']
    if situacao:
        if aluno['media'] >= 7.0:
            sit = 'Boa'
        elif aluno['media'] >= 5:
            sit = 'RAZOÁVEL'
        else:
            sit = 'ruim'
        aluno['situaçao'] = sit
    return aluno


# Programa Principal
resp = nota(3.5, 10, 6.5)
resp1 = nota(3.5, 2, 6.5, 2, 7, 4, situacao=True)
print(resp)
print(resp1)
help(nota)
