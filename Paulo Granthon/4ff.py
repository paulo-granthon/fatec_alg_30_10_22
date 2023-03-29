# Versão for fun utilizando inumeras tecnicas não permitidas na atividade reduzindo a quantidade de linhas para 1/8 da oficial e a legibilidade para 0.01%
L = [[(lambda v, n, p, x=x: [v[0] + 1, (v[1] * (1 - x)) + n] + v[2:] if p != None and n == p + 1 - x else [1, n] + v[2:]), (lambda v: v[:2] + v[:2] if v[0] > v[2] or (v[0] == v[2] and v[1] > v[3]) else v), [0] * 4] for x in range(2)]
for n, p in zip(nums, [None] + nums[:-1]): L = (lambda L, n, p: [[L[x][0], L[x][1]] + [L[x][1](L[x][0](L[x][2], n, p))] for x in range(2)])(L, n, p)
for x in range(2): print('*4.'+ str(x + 1) + ') ' + (' | '.join([['contagem: ', ['soma: ', 'valor: '][x]][v] + str(L[x][2][2 + v]) for v in range(2)])))
