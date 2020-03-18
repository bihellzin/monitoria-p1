n = int(input('Insira o valor de N: '))

ehPrimo = True

for i in range(2, n):
    print(i)
    if n % i == 0:
        ehPrimo = False
        i = n + 1

if ehPrimo == True:
    print(n, 'é primo')

else:
    print(n, 'não é primo')
