# geração de lista com numeros aleatorios para teste do algoritmo
from random import randint
nums = [randint(0, 9) for _ in range(150)]



# Resolução oficial da atividade utilizando if, else e for
count_A, sum_A, max_count_A, max_sum_A = 0, 0, 0, 0
count_B, val_B, max_count_B, max_val_B = 0, 0, 0, 0
prev = None
for num in nums:
    if prev == None or num != prev + 1:
        count_A = 1
        sum_A = num
    else:
        count_A += 1
        sum_A += num
    if count_A > max_count_A or (count_A == max_count_A and sum_A > max_sum_A):
        max_count_A = count_A
        max_sum_A = sum_A
    if num != prev:
        count_B = 1
        val_B = num
    else:
        count_B += 1
        val_B = num
    if count_B > max_count_B or (count_B == max_count_B and val_B > max_val_B):
        max_count_B = count_B
        max_val_B = val_B
    prev = num
print(f'4.1) contagem da sequencia: {max_count_A} | soma: {max_sum_A}')
print(f'4.2) contagem da sequencia: {max_count_B} | valor: {max_val_B}')
