n = int(input('Insira o valor de N: '))

cont = 2
ehPrimo = True

while cont < n and ehPrimo == True:
    if n % cont == 0:
        ehPrimo = False

    cont += 1

if ehPrimo:
    print(n, 'é primo')

else:
    print(n, 'não é primo')
