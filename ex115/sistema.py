from ex115.lib.interface import *

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar noa Pessoa', 'Sair do Sistema'])
    if resposta == 0:
        print('Opção 1')
    elif resposta == 1:
        print('Opção 2')
    elif resposta == 2:
        cabecalho('Saindo do sistema.. Até logo!')
        break
    else:
        print('\033[31mERRO! Tente novamente.\033[m')
