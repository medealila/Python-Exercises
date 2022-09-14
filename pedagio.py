import math

comprimento, distanciaPedagios = [int(w) for w in input().split()]
quilometroPercorrido, valorPedagio = [int(w) for w in input().split()]

quantidadePedagios = math.floor(comprimento / distanciaPedagios)
valorTotalPedagios = quantidadePedagios * valorPedagio
valorQuilometro = quilometroPercorrido * comprimento
custoViagem = round(valorTotalPedagios + valorQuilometro)

print(custoViagem)