import turtle

win = turtle.Screen()
win.screensize(300,300)
win.bgcolor('black')
t = turtle.Turtle()
t.color('cyan')

t.width(3)

for i in range(3):
    t.forward(100)
    t.left(360/3)

t.penup()
t.left(90)
t.forward(65)
t.right(90)
t.pendown()

for i in range(3):
    t.forward(100)
    t.right(360/3)


turtle.done()