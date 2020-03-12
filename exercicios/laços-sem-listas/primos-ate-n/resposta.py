n = int(input('Quer saber os números primos até qual número ? '))

num = 2

while num <= n:
    ehPrimo = True
    cont = 2

    while cont < num and ehPrimo == True:
        if num % cont == 0:
            ehPrimo = False
            
        cont += 1

    if ehPrimo == True:
      print(num)
    num += 1