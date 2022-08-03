def cabecalho(comand=''):
    """
    -> Função para realizar a personalização de frases.
    :param comand: Valor opcional, indica a frase que será escrita.
    :return: não possui retorno.
    :author: Vinicius Andrade
    """
    if comand.lower() == 'fim':
        frase = 'ATÉ LOGO!'
        print('\033[1;33;41m', end='')
    elif comand != '':
        frase = f'Acessando o manual do comando \'{comand}\''
        print('\033[1;30;46m', end='')
    else:
        frase = 'SISTEMA DE AJUDA PyHELP'
        print('\033[1;30;102m', end='')
    print('~' * (len(frase) + 4))
    print(f'{frase:^{len(frase) + 4}}')
    print('~' * (len(frase) + 4))
    print('\033[m', end='')


def manual(instrucao):
    """
    -> Função criada para apresentar o manual de suas funções e bibliotecas
    :param instrucao: O nome da biblioteca que deseja descobrir o manual.
    :return: Manual descrito.
    :author: Vinicius Andrade
    """
    cabecalho(instrucao)
    print(f'\033[1;31;40m', end='')
    help(instrucao)
    print('\033[m')


# Programa Principal
while True:
    cabecalho()
    resp = input('Função ou Biblioteca > ')
    if resp.lower() == 'fim':
        cabecalho(resp)
        break
    else:
        manual(resp)
