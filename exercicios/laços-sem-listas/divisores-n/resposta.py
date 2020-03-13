n = int(input('Digite o valor de N: '))

divisores = 0
cont = 1

while cont <= n:
    if n % cont == 0:
        divisores = divisores + 1
        print(cont)
    
    cont = cont + 1

if divisores > 2:
    print('O número %d não é primo e possui %d divisores' %(n, divisores)) 

else:
    print('O número %d é primo e possui %d divisores' %(n, divisores)) 
