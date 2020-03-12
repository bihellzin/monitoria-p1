area = int(input("Digite a área a ser pintada: "))

litros = area//3
if area % 3 > 0:
    litros = litros + 1

latas = litros//18
if litros % 18 > 0:
    latas = latas + 1

print("Você precisara de", latas, "latas.")
print("Você vai pagar R$", latas * 80)