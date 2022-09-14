horas = int(input("Digite as horas mensais: "))
horasExtras = int(input("Digite as horas extras trabalhadas: "))

valorHoraNormal = horas * 12.5
valorHorasExtras = horasExtras * (20 / 100)
salarioBruto = valorHoraNormal + valorHorasExtras
inss = salarioBruto * (9 / 100)
impostoRenda = salarioBruto * (13 / 100)

salarioLiquido = salarioBruto - inss - impostoRenda

print("- Salário Bruto: {:.2f}".format(salarioBruto))
print("- IR (13%): {:.2f}".format(impostoRenda))
print("- INSS (9%): {:.2f}".format(inss))
print("- Salário Líquido: {:.2f}".format(salarioLiquido))