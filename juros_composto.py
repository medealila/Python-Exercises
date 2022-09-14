capital = float(input("Digite o valor de capital em reais: "))
meses = int(input("Digite o número de meses: "))
taxa = float(input("Digite o valor da taxa: ")) / 100

montante = capital * (1 + taxa) ** meses

print("O valor do montante é de: {:.2f}".format(montante))