
N = None
while N is None or N < 50:
    N = int(input("Informe o valor de N (≥ 50): "))

H, S, P = 0, 0, 0
x = 2

for num in range(1, N + 1):
    if num % 2 == 0 or num == 1:
        H += ((num * 2) - 1) / num
        if num == 1:
            S += num / (num * num)
        else:
            S -= num / (num * num)
    else:
        H -= ((num * 2) - 1) / num
        S += num / (num * num)
    prime = None
    while prime is None:
        for i in range (2, x):
            if x % i == 0:
                break
        else:
            prime = x
        x += 1
    P += prime / (((num * 2) - 1) ** 3)
print(f'N: {N}  \t| H: {H}  \t| S: {S}  \t| P: {P}')


