import random
import turtle

def draw_circle(x,y,r):
    turtle.penup()
    turtle.goto(x,y)
    turtle.stamp()
    turtle.goto(x,y-r)
    turtle.setheading(0)
    turtle.pendown()
    turtle.circle(r)

turtle.shape('turtle')
while True:
    draw_circle(random.randint(-300,300),random.randint(-300,300),random.randint(100,200))

turtle.exitonclick()