import turtle

caneta = turtle.Turtle()
caneta.speed(0)
raio = 50
caneta.right(90)

for i in range(2):
    caneta.begin_fill()
    caneta.color('black')
    caneta.circle(raio)
    caneta.end_fill()
    caneta.color('blue')
    caneta.circle(raio+30)
    caneta.circle(raio+60)
    caneta.circle(raio+90)
    caneta.right(180)
    
caneta.up()
caneta.fd(5*raio)
caneta.color('magenta')
caneta.down()

for nariz in range(72):
    caneta.fd(50)
    caneta.right(180)
    caneta.fd(50)
    caneta.right(5)
    
caneta.seth(270)
caneta.up()
caneta.fd(2*raio - 50)
caneta.right(90)
caneta.fd(2*raio - 15)
caneta.pensize(7)
caneta.right(245)
caneta.color('red')
caneta.down()
caneta.circle(90, 130)
    
    
turtle.done()