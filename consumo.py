distancia = int(input("Digite a distância percorrida em quilômetros: "))
combustivel_gasto = float(input("Digite o total de combustível gasto em litros: "))

consumo = distancia / combustivel_gasto

print("O consumo médio do automóvel é de: {:.3f}".format(consumo), "km/l")