distancia = float(input('Qual a distancia da viagem?\n- '))
if distancia <= 200:
    valorFinal = distancia * 0.50
else:
    valorFinal = distancia * 0.45
print(f'O valor a ser pago na sua viagem é de \033[4;35mR${valorFinal:.2f}\033[m')
