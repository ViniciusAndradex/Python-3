while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 36)
    for c in range(1, 11):
        print(f'{n} * {c :2} = {n * c:3}')
    print('-' * 36)
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')
