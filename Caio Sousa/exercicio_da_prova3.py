pais_a = 15000
pais_b = 45000
pais_c = 65000

tax_cresc_a = 0.100
tax_cresc_b = 0.050
tax_cresc_c = 0.025

C_var = pais_c * 0.23
pais_c = C_var + pais_c

controlador1 = 0
controlador2 = 0

while pais_a < pais_b:
    pais_a = pais_a + (pais_a * tax_cresc_a)
    pais_b = pais_b + (pais_b * tax_cresc_b)
    
    controlador1 +=  1

print(f'ao final de  {controlador1} o país A ficou com {pais_a} habitantes, e o país B ficou com {pais_b}')

pais_a = 15000

while pais_a < pais_c:
    pais_a = pais_a + (pais_a * tax_cresc_a)
    pais_c = pais_c + (pais_c * tax_cresc_c)
    controlador2 = controlador2 + 1

print(f'levaria {controlador2} anos para a cidade A ultrapassar a cidade C em 23%')
print(f'o pais A ficou com {pais_a} habitantes, e o país b ficou com {pais_c} habitantes')

