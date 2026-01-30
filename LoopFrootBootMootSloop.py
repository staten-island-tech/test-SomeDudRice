
import turtle
from turtle import *
t = Turtle()
#LOOPS IN PYTHON

# "makes 0 1 2"
# for i in range (3):
#     print(i)

# makes square
# for i in range(4):
#     t.forward(100)
#     t.left(90)

def square():
 for i in range(60):
    print (i)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(95)
    
square()
turtle.done()

