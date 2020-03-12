valor_compras = int(input('Insira o total das compras: '))

notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0
notas_2 = 0
moeda_1 = 0

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

else:
    moeda_1 = valor_compras

print('O troco deu', notas_100, 'notas de 100,', notas_50, 'notas de 50,', notas_20, 'notas de 20,', notas_10, 'notas de 10,', notas_5, 'notas de 5,', notas_2, 'notas de 2', 'e', moeda_1, 'moedas de 1 real' )