import turtle
import math

construtor = turtle.Turtle()

x = 100

#retângulo
construtor.begin_fill()
construtor.fillcolor('brown')
for i in range(2):
    construtor.forward(2*x)
    construtor.left(90)
    construtor.forward(x)
    construtor.left(90)
construtor.end_fill()
    
#porta
construtor.forward(x/3)
construtor.left(90)

construtor.begin_fill()
construtor.fillcolor('chocolate')
construtor.forward(2*x/3)
construtor.right(90)
construtor.forward(x/3)
construtor.right(90)
construtor.forward(2*x/3)
construtor.end_fill()

#janela 01
construtor.up()
construtor.left(90)
construtor.forward(x/4)
construtor.left(90)
construtor.forward(x/3)
construtor.down()

construtor.begin_fill()
construtor.fillcolor('white')
for i in range(4):
    construtor.forward(x/3)
    construtor.right(90)
construtor.end_fill()
    
#janela 02
construtor.up()
construtor.right(90)
construtor.forward(x/2)
construtor.down()

construtor.begin_fill()
construtor.fillcolor('white')
for i in range(4):
    construtor.forward(x/3)
    construtor.left(90)
construtor.end_fill()
    
#telhado
construtor.up()
construtor.left(90)
construtor.forward(2*x/3)
construtor.right(90)
construtor.forward(x/3 + x/4)
construtor.left(135)
construtor.down()

construtor.begin_fill()
construtor.fillcolor('chocolate')
construtor.forward(x * math.sqrt(2))
construtor.left(90)
construtor.forward(x * math.sqrt(2))

construtor.forward(x/5)
construtor.left(135)
construtor.forward(2 * x/7 + 2 * x)
construtor.left(135)
construtor.forward(x/5)
construtor.end_fill()


turtle.done()