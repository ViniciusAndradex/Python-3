n = int(input('Digite um numero: '))
n1 = int(input('Digite outro numero: '))
n2 = int(input('Digite outro numero: '))
menor = n
if n2 > n1 < n:
    menor = n1
if n > n2 < n1:
    menor = n2
maior = n
if n < n1 > n2:
    maior = n1
if n < n2 > n1:
    maior = n2
print(f'Maior: \033[1;33m{maior}\033[m\nMenor: \033[1;31;107m{menor}\033[m')
