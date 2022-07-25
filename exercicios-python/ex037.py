decimal = int(input('Digite um número: '))
menu = int(input('''\033[1;35mCONVERSOR DE BASES NUMERICAS\033[m
\033[1;31m[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL
\033[m- \033[1;34m'''))
if menu == 1:
    print(f'{decimal} -> BINARIO: {bin(decimal)[2:]}')
elif menu == 2:
    print(f'{decimal} -> OCTAL: {oct(decimal)[2:]}')
elif menu == 3:
    print(f'{decimal} -> HEXADECIMAL: {hex(decimal)[2:]}')
else:
    print('OPÇÃO INVALIDA')
