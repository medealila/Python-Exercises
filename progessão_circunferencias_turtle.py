import turtle

caneta = turtle.Turtle()
caneta.speed(0)
raio = 5

for i in range(8):
    raioAntigo = raio
    tangenteInterna = raioAntigo + raio + 5
    caneta.up()
    caneta.begin_fill()
    caneta.color('orange')
    caneta.circle(raio)
    caneta.end_fill()
    caneta.fd(tangenteInterna)
    raio = raio + 5


turtle.done()
