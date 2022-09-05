import turtle

caneta = turtle.Turtle()
caneta.speed(0)
caule = 200

#caule
caneta.pensize(4)
caneta.left(90)
caneta.fd(caule)

#folha
caneta.pensize(1)
caneta.left(180)
caneta.fd(caule/2 + 20)
caneta.left(90)
caneta.circle(60, 60)
caneta.seth(180)
caneta.circle(60, 60)
caneta.seth(90)
caneta.fd(caule/2 + 20)

caneta.seth(40)

#petalas
angulo = 90
for petala in range(7):
    caneta.circle(60, angulo)
    caneta.left(180 - angulo)
    caneta.circle(60, angulo)
    caneta.left(180 - angulo)
    caneta.left(360/7)

turtle.done()