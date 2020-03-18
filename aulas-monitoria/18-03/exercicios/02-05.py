fibn = int(input('Insira o valor de N: '))

fib0 = 0
fib1 = 1

cont = 1

while cont < fibn:
    temp = fib1
    fib1 = fib1 + fib0
    fib0 = temp

    cont += 1

print(fib1)
