import turtle

win = turtle.Screen()
win.screensize(300,300)
win.bgcolor('black')
t = turtle.Turtle()
t.color('red')
size = 10

for i in range(200):
    t.forward(size)
    t.right(90)
    size+=2



turtle.done