velocidadeCarro = float(input('Digite a velocidade do seu carro em Km: '))
if velocidadeCarro > 80.0:
    multa = (velocidadeCarro - 80.00) * 7.00
    print(f'Sua multa foi de R${multa:.2f}')
else:
    print('Parabéns você não foi multado')
