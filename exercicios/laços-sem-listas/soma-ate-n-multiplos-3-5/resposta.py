n = int(input('Digite o valor de N: '))

cont = 0
soma = 0

while cont < n:
    if cont % 3 == 0 or cont % 5 == 0:
        soma = soma + cont

    cont = cont + 1
    
print(soma)