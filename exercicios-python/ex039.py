from datetime import date

anoNascimento = int(input('Ano de nascimento: '))
idade = date.today().year - anoNascimento
if idade < 18:
    falta = 18 - idade
    print(f'Ainda faltam {falta} anos para se alistar!')
elif idade > 18:
    passou = idade - 18
    print(f'Já passaram {passou} anos do seu alistamento!')
else:
    print(f'\033[1;35;42mVocê possui a idade do alistamento, {idade} anos. CUIDA!\033[m')
