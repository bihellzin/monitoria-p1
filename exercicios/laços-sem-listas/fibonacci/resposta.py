n = int(input('Insira qual o enésimo número da sequência de Fibonacci você quer: '))

fib0 = 0
fib1 = 1

cont = 1

while cont < n:
    temp = fib1
    fib1 = fib1 + fib0
    fib0 = temp
    cont += 1

print(fib1) 