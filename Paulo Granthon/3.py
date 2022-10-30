A, B = 15000, 45000
pA, pB  = .1, .05
a = 0
while A < B:
    A += A*pA
    B += B*pB
    a += 1
print(f'A excede B em {a} anos')
A, C = 15000, 65000
pA, pC  = .1, .025
a = 0
while A < C * 1.23:
    A += A*pA
    C += C*pC
    a += 1
print(f'A excede C em 23% em {a} anos')
