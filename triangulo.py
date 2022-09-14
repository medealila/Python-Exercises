lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

variavelA = bool(lado1 + lado2 > lado3)
variavelB = bool(lado2 + lado3 > lado1)
variavelC = bool(lado1 + lado3 > lado2)

print(variavelA and variavelB and variavelC)