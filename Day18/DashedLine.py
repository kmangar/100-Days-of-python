from turtle import Turtle

john = Turtle()

john.shape('turtle')

john.color('black')

for _ in range(20):
    john.forward(10)
    john.pu()
    john.forward(10)
    john.pd()


