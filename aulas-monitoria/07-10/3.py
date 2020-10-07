'''
Faça um programa que diz se um elemento está inserido na lista ou não.
'''

lista = [1, 2, 3, 4, 5]

elemento = int(input('Insira o elemento a ser procurado: '))
achou = False

for i in lista:
    if i == elemento:
        achou = True

if achou == True:
    print('Achei o elemento')

else:
    print('Elemento nao esta na lista')

