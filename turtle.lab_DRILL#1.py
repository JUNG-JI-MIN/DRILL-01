import turtle

def turtle_moveW():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)
def turtle_moveA():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)
def turtle_moveS():
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(50)
def turtle_moveD():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)
def reset():
    turtle.reset()

turtle.shape('turtle')
turtle.onkey(turtle_moveW, 'w')
turtle.onkey(turtle_moveA, 'a')
turtle.onkey(turtle_moveS, 's')
turtle.onkey(turtle_moveD, 'd')
turtle.listen()
turtle.mainloop()
