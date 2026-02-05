
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

# circle square vietnam flashback
# def square():
#  for i in range(60):
#     print (i)
#     t.forward(100)
#     t.right(90)
#     t.forward(100)
#     t.right(90)
#     t.forward(100)
#     t.right(90)
#     t.forward(100)
#     t.right(95)
# square()
# turtle.done()

# dont have to manually put in values
# sidelength = 100
# rotate = 90
# def triangle(x,y):
#     for i in range(4):
#         t.forward(x)
#         t.left(y)
# triangle(100,90)


# def Squarespiral():
#  for i in range (60):
#      def square (length , y):
#             t.forward(length)
#             t.right(y)
#             t.forward(length)
#             t.right(y)
#             t.forward(length)
#             t.right(y)
#             t.forward(length)
#             t.right(y)
#             t.right(5)
            
            
            
#      square (i*5 + 5, 90)
# Squarespiral()
def Squarespiral():
  for i in range (60):
      def square (length , y):
             t.forward(length)
             t.right(y)
             t.forward(length)
             t.right(y)
             t.forward(length)
             t.right(y)
             t.forward(length)
             t.right(y)
             t.forward(length)
             t.right(y)
             t.right(5)
             
            
            
            
      square (i*5 + 5, 144)
Squarespiral()