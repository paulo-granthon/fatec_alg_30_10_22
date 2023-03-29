salario = int(input("Insira seu salário: "))
vendas = int(input("Insira o total de suas vendas: "))
if vendas <= 1500:
    print(salario + (vendas * 0.05))
else:
    print(salario + 75 + ((vendas - 1500) * 0.07))
