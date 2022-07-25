r1 = int(input('Digite o primeiro segmento de reta: '))
r2 = int(input('Digite o segundo segmento de reta: '))
r3 = int(input('Digite o terceiro segmento de reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É POSSÍVEL FORMAR UM TRIÂNGULO!')
    if r1 == r2 == r3:
        print('\033[1;36mCATEGORIA: EQUILÁTERO\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[1;32mCATEGORIA: ESCALENO\033[m')
    else:
        print('\033[1;37;42mCATEGORIA: ISÓSCELES\033[m')
else:
    print('NÃO É POSSÍVEL FORMA TRIÂNGULO')
