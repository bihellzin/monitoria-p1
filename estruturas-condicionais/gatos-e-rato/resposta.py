gato_A = int(input('Insira a posição do gato A: '))
gato_B = int(input('Insira a posição do gato B: '))
rato = int(input('Insira a posição do rato: '))

distancia_gatoA_rato = gato_A - rato

if distancia_gatoA_rato < 0:
  distancia_gatoA_rato = distancia_gatoA_rato * -1


distancia_gatoB_rato = gato_B - rato

if distancia_gatoB_rato < 0:
  distancia_gatoB_rato = distancia_gatoB_rato * -1


if distancia_gatoA_rato < distancia_gatoB_rato:
  print('Gato A pega o rato')

elif distancia_gatoB_rato < distancia_gatoA_rato:
  print('Gato B pega o rato')

else:
  print('O rato escapou porque os gatos brigaram')