num = [2, 5, 9, 1]
print(num)
num[1] = 3
print(num)
num.append(9)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f'Lista com tamanho de {len(num)}')
num.insert(2, 0)
print(num)
num.pop()
print(num)
num.pop(2)
print(num)
num.remove(9)
print(num)
print('*' * 50)
num = [2, 5, 9, 1]
print(num)
if 4 in num:
    num.remove(4)
    print(num)
else:
    print('Valor 4 não está na list.')
