# Recebe-se o valor do usuário
n = int(input('Insira um número para verificar se é palíndromo: '))

# A variável aux receberá o n dado pelo usuário, pois o n será utilizado para fazermos a comparação posteriormente
aux = n
# A variável do palíndromo é igual a zero, pois iremos incrementar o seu valor a cada iteração
palindromo = 0

while aux != 0:
    # A cada iteração, multiplicaremos o valor atual do palíndromo por 10 e adicionaremos o resto da divisão por 10 do valor
    # auxiliar. Após isso, aux será decrementado
    palindromo = (palindromo * 10) + (aux % 10)
    aux = aux // 10


# Caso o valor do palíndromo seja igual ao n inicial, o número é palíndromo, caso contrário, não é.
if palindromo == n:
    print('O número é palindromo')

else:
    print('O número não é palindromo')
