indice = int(input('Insira o indice que deseja inserir o valor: '))
elemento = int(input('Insira o valor do elemento a ser inserido: '))

lista = [1, 2, 4, 5]

temp = []
# temp = lista[indice:]

for i in range(indice, len(lista)):
    temp.append(lista[i])

# indice = 2
# temp = [4, 5]

nova_lista = []

for i in range(indice):
    nova_lista.append(lista[i])


nova_lista.append(elemento)

print(nova_lista + temp)
