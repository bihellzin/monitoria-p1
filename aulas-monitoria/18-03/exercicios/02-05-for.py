n = int(input('Insira o valor de N: '))

fib0 = 0
fib1 = 1

for i in range(1, n):
    temp = fib1
    fib1 = fib1 + fib0
    fib0 = temp

print(fib1)
