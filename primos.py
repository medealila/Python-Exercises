import math

n = int(input())

resposta1 = round(n/math.log(n), 1)
resposta2 = round((1.25506)*(n/math.log(n)), 1)

print(resposta1, resposta2)