area = int(input("Digite a area a ser pintada: "))

numLitros = area / 18
numGaloes = max(round(numLitros / 3.6), 1)
valor = numGaloes * 25

print("Área de cobertura: ", area)
print("Número de galões: ", numGaloes)
print("Valor a ser pago: R$ {:.2f}".format(valor))