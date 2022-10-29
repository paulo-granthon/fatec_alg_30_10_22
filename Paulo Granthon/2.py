
# resolução oficial
salario = int(input("Insira seu salário: "))
vendas = int(input("Insira o total de suas vendas: "))
if vendas <= 1500:
    print(salario + (vendas * 0.05))
else:
    print(salario + 75 + ((vendas - 1500) * 0.07))



# versão forfun
# print((lambda s, v: s + (v * 0.05) if v <= 1500 else s + 75 + ((v - 1500) * 0.07))(int(input("Salário: ")), int(input("Vendas: "))))

