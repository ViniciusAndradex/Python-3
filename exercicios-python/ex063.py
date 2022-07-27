n = int(input('Digite um número: '))
v1 = -1
v2 = 1
v3 = cont = 0

while cont < n:
    v3 = v1 + v2
    v1 = v2
    v2 = v3
    print(v3, end=' -> ')
    cont += 1
print('FIM')
