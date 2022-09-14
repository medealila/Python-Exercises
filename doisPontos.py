import math

x1, y1 = [float(w) for w in input().split()]
x2, y2 = [float(w) for w in input().split()]

ditancia = float(round(math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2)), 4))

print(ditancia)