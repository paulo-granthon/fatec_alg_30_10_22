salario_fixo = int(input('digite seu sálario '))
Taxa_min = 0.05
Taxa_max = 0.07
vendas= int(input('digite a valor de vendas que efetuou esse mês '))

tax_max_vendas = 1500 * Taxa_min 

if vendas < 1500:
    salario_final = salario_fixo + (vendas*0.05)

else:
    salario_final = salario_fixo + (0.07*(vendas-1500)) + tax_max_vendas

print(f"sua renda no final deste mês é de {salario_final}")