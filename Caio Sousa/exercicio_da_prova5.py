N= None
while N is None or N < 50:
    N = int(input("informe o valor de N, sendo ele maior ou igual a 50 "))

H,S,P = 1, 1, 2
x = 3

for num in range(2, N + 1):
    if num % 2 == 0:
        H+= ((num * 2)-1)/ num 
        S-= num / (num*num)
    else:
        H-= ((num*2) - 1)/num
        S+= num/ (num*num)
    prime = None
    while prime is None:
        for i in range (2, x):
            if x % i == 0:
                break
        else:
            prime = x
        x += 1
    P += prime / (((num * 2) - 1) ** 3)

print(f'usando {N}')
print(f'o resultado de h é de {H}')
print(f'o resultado de s é de {S}')
print(f'e o resultado de p é igual a {P}')
