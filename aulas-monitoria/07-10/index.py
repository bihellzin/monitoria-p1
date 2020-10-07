elemento = int(input('Insira o valor do elemento a ser buscado: '))

indice = 0

lista = [5,8,3,1,0,2]

for i in range(len(lista)):
    if elemento == lista[i]:
        print(i)

    
