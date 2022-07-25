distancia = float(input('Qual a distancia da viagem?\n- '))
valorFinal = float
if distancia <= 200:
    valorFinal = distancia * 0.50
else:
    valorFinal = distancia * 0.45
print(f'O valor a ser pago na sua viagem é de R${valorFinal:.2f}')
