tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
         'mercado', 'programador', 'futuro')
for c in tupla:
    print(f'Na palavra {c.upper()} temos ', end='')
    for vogal in c:
        if vogal in 'aeiou':
            print(vogal, end=' ')
    print()
