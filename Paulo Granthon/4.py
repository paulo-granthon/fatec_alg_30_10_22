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






# Versão for fun utilizando inumeras tecnicas não permitidas na atividade reduzindo a quantidade de linhas para 1/8 da oficial e a legibilidade para 0.01%
# L = [[(lambda v, n, p, x=x: [v[0] + 1, (v[1] * (1 - x)) + n] + v[2:] if p != None and n == p + 1 - x else [1, n] + v[2:]), (lambda v: v[:2] + v[:2] if v[0] > v[2] or (v[0] == v[2] and v[1] > v[3]) else v), [0] * 4] for x in range(2)]
# for n, p in zip(nums, [None] + nums[:-1]): L = (lambda L, n, p: [[L[x][0], L[x][1]] + [L[x][1](L[x][0](L[x][2], n, p))] for x in range(2)])(L, n, p)
# for x in range(2): print('*4.'+ str(x + 1) + ') ' + (' | '.join([['contagem: ', ['soma: ', 'valor: '][x]][v] + str(L[x][2][2 + v]) for v in range(2)])))





