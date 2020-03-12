n = int(input('Insira um valor para N: '))

aux = n
soma = 0

while aux != 0:
    soma = soma + (aux % 10)
    aux = aux // 10

print(soma)