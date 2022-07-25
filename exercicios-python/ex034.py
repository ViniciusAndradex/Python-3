salario = float(input('Digite seu salário: R$'))
if salario > 1250.00:
    newSalario = (salario * 10 / 100) +salario
else:
    newSalario = (salario * 15 / 100) + salario
print(f'Seu novo salário é \033[4;35;40mR${newSalario:.2f}\033[m')
