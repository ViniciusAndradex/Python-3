from datetime import date

anoNascimento = int(input('Ano de nascimento: '))
idade = date.today().year - anoNascimento
if idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para se alistar!')
    print(f'Ano de alistamento: {date.today().year + saldo}')
elif idade > 18:
    saldo = idade - 18
    print(f'Já passaram {saldo} anos do seu alistamento!')
    print(f'Ano de alistamento: {date.today().year - saldo}')
else:
    print(f'\033[1;35;42mVocê possui a idade do alistamento, {idade} anos. CUIDA!\033[m')
    print(f'Ano de alistamento: {date.today().year}')
