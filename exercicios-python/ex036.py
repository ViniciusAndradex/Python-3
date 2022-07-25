valorCasa = float(input('Valor da Casa: R$'))
salario = float(input('Qual seu saslário R$'))
anos = int(input('Em quantos anos quer pagar?\n- '))
prestacaoMensal = valorCasa / (anos * 12)
salario30 = salario * 30 / 100
if prestacaoMensal > salario30:
    print(f'EMPRESTIMO NEGADO A PRESTAÇAO MENSAL É DE \033[4;34mR${prestacaoMensal:.2f}\033[m E EXCEDE 30% DO SEU SALARIO!')
elif prestacaoMensal < salario30:
    print(f'EMPRESTIMO APROVADO VALOR DA PRESTAÇAO \033[4;33mR${prestacaoMensal:.2f}')
