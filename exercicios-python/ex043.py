altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura**2)
print(f'INDICE: {imc:.2f}')
if imc < 18.5:
    print('\033[1;30mABAIXO DO PESO')
elif imc < 25:
    print('\033[1;32mPESO IDEAL')
elif imc < 30:
    print('\033[1;33mSOBREPESO')
elif imc < 40:
    print('\033[1;34mOBESIDADE')
else:
    print('\033[1;37mOBESIDADE MÓRBIDA')
