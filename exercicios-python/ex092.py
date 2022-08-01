from datetime import date
trabalho = dict()
trabalho['nome'] = str(input('Nome: ')).strip().capitalize()
nasc = int(input('Data de Nascimento: '))
trabalho['idade'] = date.today().year - nasc
trabalho['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalho['ctps'] > 0:
    trabalho['contratação'] = int(input('Ano de Contratação: '))
    trabalho['salario'] = float(input('Salário: R$'))
    trabalho['aposentadoria'] = (trabalho['contratação'] + 35 - date.today().year) + trabalho['idade']
print('-' * 20)
for k, v in trabalho.items():
    print(f'{k} tem o valor {v}')
