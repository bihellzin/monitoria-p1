n = int(input('Digite o valor de N: '))
x = int(input('Digite o x: '))
y = int(input('Digite o valor de y: '))

cont = 0
soma = 0

while cont < n:
    if cont % x == 0 or cont % y == 0:
        soma = soma + cont

    cont = cont + 1
    
print(soma)