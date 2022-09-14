nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

nota1_peso = int(nota1 * 2)
nota2_peso = int(nota2 * 3)
nota3_peso = int(nota3 * 5)

soma_pesos = 2 + 3 + 5

media_ponderada = (nota1_peso + nota2_peso + nota3_peso) / soma_pesos

print("MEDIA: ", media_ponderada)