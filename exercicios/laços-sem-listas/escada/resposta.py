# Usuário digita a quantidade de degraus que quer imprimir
n = int(input('Insira a quantidade de degraus: '))

# Essas variáveis não são essenciais, mas acho que fica mais fácil de compreender a questão
jogo_da_velha = '#'
espacos = ' '

# O contador é iniciado em 1 para que não seja necessário utilizar muita aritmética dentro do print
cont = 1

# O contador é iterado até que a quantidade de vezes que o bloco de código é executado dentro do laço 
# seja igual ao n dado pelo usuário
while cont <= n:
    print(espacos * (n - cont) + (jogo_da_velha * cont))
    cont += 1
