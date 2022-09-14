larguraConteiner, comprimentoConteiner, alturaConteiner = [int(x) for x in input().split()]
larguraNavio, comprimentoNavio, alturaMaxNavio = [int(x) for x in input().split()]

areaNavio = larguraNavio * comprimentoNavio
volumeConteiner = larguraConteiner * comprimentoConteiner * alturaConteiner
totalConteiner = min(volumeConteiner // areaNavio), alturaMaxNavio

print(totalConteiner)