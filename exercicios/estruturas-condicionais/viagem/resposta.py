km = float(input('Digite quantos km terá a viagem: '))

if km > 200:
    valor_viagem = (km * 0.45)

else:
    valor_viagem = (km * 0.50)

print('O valor total da viagem será de R$%.2f' %(valor_viagem))