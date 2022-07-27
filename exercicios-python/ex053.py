frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(' ', '')
palindromo = frase[::-1]
# x = ''
# for c in range(len(frase)-1, -1, -1):
#    x += frase[c]
# if x == frase:
#    print('É um PALINDROMO')
# else:
#    print('Não é um PALINDROMO')
print('*-' * 9)
print(frase)
print(palindromo)
print('*-' * 9)
if palindromo == frase:
    print('A frase \033[1;34mé\033[m um PALINDROMO!')
else:
    print('A frase \033[1;31mnão\033[m é um PALINDROMO!')
