lista = list()
lista.append(input('Digite uma expressão: ').strip())
if (lista[0].count('(') + lista[0].count(')')) % 2 == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
