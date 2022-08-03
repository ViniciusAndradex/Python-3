def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade < 16:
        opc = 'NÃO VOTA'
    elif idade >= 65 or idade < 18:
        opc = 'VOTO OPCIONAL'
    else:
        opc = 'VOTO OBRIGATÓRIO'
    return f'Com {idade} anos: {opc}'


# Programa Principal
print('-' * 20)
print(voto(ano=int(input('Ano de Nascimento: '))))
