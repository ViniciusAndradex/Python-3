r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('\033[1;32;47mE POSSIVEL FORMAR UM TRIANGULO\033[m')
else:
    print('\033[1;31;46mNAO E POSSIVEL FORMAR UM TRIANGULO\033[m')
