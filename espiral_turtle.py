import turtle

caneta = turtle.Turtle()
caneta.speed(0)

for distancia in range(20, 200, 1):
    caneta.fd(distancia)
    caneta.right(88)

turtle.done()