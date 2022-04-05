import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow','gray']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(50):
    t.pencolor(colors[x%7])
    t.width(x//200+5)
    t.fillcolor("orange")
    t.forward(x)
    t.speed(0)
    t.forward(20)
    t.right(20)
    t.left(15)
    t.forward(40)
    t.right(60)
    t.forward(-30)
    t.right(20)
    t.left(50)
