lista = list()
#expr = str(input('Digite a expressão: ')), PREFIRO A MINHA Lógica.
lista.append(input('Digite uma expressão: ').strip())
if (lista[0].count('(') + lista[0].count(')')) % 2 == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
#for simb in expr:
#    if simb == '(':
#        lista.append('(')
#    elif simb == ')':
#        if len(lista) > 0:
#            lista.pop()
#        else:
#            lista.append(')')
#            break
#if len(lista) == 0:
#    print('Sua expressão está válida!')
#else:
#    print('Sua expressão está errada!')
