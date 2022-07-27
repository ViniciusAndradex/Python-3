num = int(input('Digite um número: '))
fact = 1
print(f'{num}! =', end=' ')
while num >= 1:
    print(f'{num}', end=' ')
    if num != 1:
        print(end='* ')
    fact *= num
    num -= 1
print(f' = {fact}')
