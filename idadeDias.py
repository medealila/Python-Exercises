import math
farinha, ovos, leite = [int(w) for w in input().split()]

farinhaReceita = farinha // 2
ovosReceita = ovos // 3
leiteReceita = leite // 5

receita = min(farinhaReceita + ovosReceita + leiteReceita)

print(receita)