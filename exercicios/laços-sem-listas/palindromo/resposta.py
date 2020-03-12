n = int(input('Insira um número para verificar se é palíndromo: '))

aux = n
palindromo = 0

while aux != 0:
    palindromo = (palindromo * 10) + (aux % 10)
    aux = aux // 10

if palindromo == n:
    print('O número é palindromo')

else:
    print('O número não é palindromo')