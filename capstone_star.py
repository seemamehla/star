import turtle
turtle.fillcolor('yellow')
turtle.penup()
turtle.setx(-200)
turtle.sety(200)
turtle.pendown()

turtle.begin_fill()
for i in range(0,5):
    turtle.forward(50)
    turtle.right(144)
turtle.end_fill()

turtle.penup()
turtle.setx(-100)
turtle.sety(200)
turtle.pendown()

turtle.begin_fill()
for i in range(0,5):
    turtle.forward(80)
    turtle.right(144)
turtle.end_fill()

turtle.penup()
turtle.setx(20)
turtle.sety(200)
turtle.pendown()

turtle.begin_fill()
for i in range(0,5):
    turtle.forward(110)
    turtle.right(144)
turtle.end_fill()