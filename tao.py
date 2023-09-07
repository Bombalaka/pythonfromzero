import turtle
import random

tao = turtle.Pen()
tao.shape('turtle')

def siliam() :
#random squece size by using random funtion 
        size = random.randint(50, 100)
        for i in range (4) :
              tao.forward(size)
              tao.left(90)

for i in range (10) :
       x = random.randint(-200, 200)
       y = random.randint(-200, 200)
       tao.up()
       tao.goto(x, y)
       tao.down()
# random color by create list and using random funtion 
       color = ['red', 'green', 'blue', 'yellow']
       select = random.choice(color)
       tao.color(select)
#excute funtion 
       siliam()
