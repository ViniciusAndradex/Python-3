from ex115.lib.interface import *
from ex115.lib.arquivo import *
from uteis.numeros import leiaInt

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar noa Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de Listar conteúdo
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('NOME: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema.. Até logo!')
        break
    else:
        print('\033[31mERRO! Tente novamente.\033[m')
