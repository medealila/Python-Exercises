import turtle
import math

caneta = turtle.Turtle()
caneta.speed(0)
circunferencia = 100
pi = 3.14
raio = circunferencia/2*pi

caneta.pensize(3)
caneta.circle(circunferencia)
caneta.up()
caneta.left(90)
caneta.fd(circunferencia)
caneta.right(85)
caneta.down()

#ponteiro minutos
caneta.pensize(3)
caneta.fd(circunferencia - 20)
caneta.left(180)
caneta.fd(circunferencia - 20)

#ponteiro horas
caneta.right(30)
caneta.pensize(4)
caneta.fd(circunferencia/2)
caneta.left(180)
caneta.fd(circunferencia/2)

#ponteiro segundos
caneta.right(235)
caneta.pensize(2)
caneta.color('red')
caneta.fd(circunferencia - 15)
caneta.left(180)
caneta.fd(circunferencia - 15)
caneta.seth(90)

#horas
for i in range(12):
    caneta.up()
    caneta.fd(circunferencia - 10)
    caneta.down()
    caneta.dot(4, "black")
    caneta.up()
    caneta.left(180)
    caneta.fd(circunferencia - 10)
    caneta.right(30)

turtle.done()