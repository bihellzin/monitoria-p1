n = int(input('Insira o valor de N: '))

for i in range(1, n + 1):
    if n % i == 0:
        print(i)
