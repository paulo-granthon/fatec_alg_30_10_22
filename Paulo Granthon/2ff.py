# Versão "for fun" da resolução do exercício 2 utilizando apenas uma linha
print((lambda s, v: s + (v * 0.05) if v <= 1500 else s + 75 + ((v - 1500) * 0.07))(int(input("Salário: ")), int(input("Vendas: "))))
