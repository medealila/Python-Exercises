nota01 = float(input("Digite a primeira nota: "))
nota02 = float(input("Digite a segunda nota: "))
nota03 = float(input("Digite a terceita nota: "))

peso01 = float(input("Digite o peso da primeira avaliação: "))
peso02 = float(input("Digite o peso da segunda avaliação: "))
peso03 = float(input("Digite o peso da terceira avaliação: "))

somaPesos = peso01 + peso02 + peso03
media = ((nota01 * peso01) + (nota02 * peso02) + (nota03 * peso03)) / somaPesos
resultado = bool(media >= 6.0)

print(resultado)