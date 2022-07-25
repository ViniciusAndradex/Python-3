from datetime import date

anoNascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - anoNascimento
print(f'IDADE: {idade}')
if idade <= 9:
    print('\033[1;31mCATEGORIA: MIRIM')
elif idade <= 14:
    print('\033[1;32mCATEGORIA: INFANTIL')
elif idade <= 19:
    print('\033[1;33mCATEGORIA: JUNIOR')
elif idade <= 25:
    print('\033[1;34mCATEGORIA: SÊNIOR')
else:
    print('\033[1;35mCATEGORIA: MASTER\033[m')
