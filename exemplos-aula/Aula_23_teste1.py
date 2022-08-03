try:
    a = int(input('Numerator: '))
    b = int(input('Denominator: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError as x:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O user preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrador foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
