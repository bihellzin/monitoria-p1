temperatura = float(input('Insira a temperatura em graus Celsius: '))
umidade_ar = float(input('Insira a porcentagem referente a umidade relativa do ar: '))

if temperatura < 10 and umidade_ar < 40:
    print('ALERTA CINZA')

elif 35 <= temperatura <= 40 and umidade_ar < 30:
    print('ALERTA LARANJA')

elif temperatura > 40 and umidade_ar < 25:
    print('ALERTA VERMELHO')

else:
    print('Nenhum alerta emitido')