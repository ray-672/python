import turtle

win = turtle.Screen()
win.screensize(300,300)
win.bgcolor('black')
t = turtle.Turtle()
t.color('red')


for i in range(6):
    t.forward(100)
    t.right(360/4)

turtle.done()