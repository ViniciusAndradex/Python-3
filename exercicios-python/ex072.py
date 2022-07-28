tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
         'treze', 'quatorze', 'quize', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número  entre 0 e 20: '))
    if 0 <= num <= 20:
        break
print(f'Você digitou o número {tupla[num]}.')
