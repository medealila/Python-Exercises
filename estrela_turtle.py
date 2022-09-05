import turtle
import math

caneta = turtle.Turtle()

caneta.begin_fill()
caneta.fillcolor('orange')
for i in range(5):
    caneta.right(144)
    caneta.fd(100)
caneta.end_fill()

turtle.done()
