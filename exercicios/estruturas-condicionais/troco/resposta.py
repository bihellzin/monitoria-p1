# Recebemos o valor das compras
valor_compras = int(input('Insira o total das compras: '))

notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0
notas_2 = 0
moeda_1 = 0

# O motivo pelo qual estou usando vários if's é o seguinte, quando utilizamos if, elif e else, o único bloco de código
# que será executa, será o primeiro que a condição for verdadeira e, mesmo que haja condicionais verdadeiras abaixo
# elas não serão executadas

# Para cada if, verificamos se a divisão inteira do valor das compras pelo número é maior que 0. 
# Caso seja verdade incrementamos a variável da nota do número com valor da divisão inteira do valor das compras 
# pelo número. 
# Em seguida, decrementamos o valor das compras, deixando apenas o resto da divisão feita anteriormente
if valor_compras // 100 > 0:
    notas_100 = valor_compras // 100
    valor_compras = valor_compras % 100

if valor_compras // 50 > 0:
    notas_50 = valor_compras // 50
    valor_compras = valor_compras % 50

if valor_compras // 20 > 0:
    notas_20 = valor_compras // 20
    valor_compras = valor_compras % 20

if valor_compras // 10 > 0:
    notas_10 = valor_compras // 10
    valor_compras = valor_compras % 10

if valor_compras // 5 > 0:
    notas_5 = valor_compras // 5
    valor_compras = valor_compras % 5

if valor_compras // 2 > 0:
    notas_2 = valor_compras // 2
    valor_compras = valor_compras % 2

if valor_compras > 0:
    moeda_1 = valor_compras
    valor_compras = 0

print('O troco deu', notas_100, 'notas de 100,', notas_50, 'notas de 50,', notas_20, 'notas de 20,', notas_10, 'notas de 10,', notas_5, 'notas de 5,', notas_2, 'notas de 2', 'e', moeda_1, 'moedas de 1 real' )
