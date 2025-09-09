import turtle
import random

def drunken_turtle():
    turtle.setheading(random.randint(0,360))
    turtle.forward(random.randint(50,100))
    turtle.stamp()
def reset():
    turtle.reset()

turtle.shape('turtle')


turtle.onkey(reset, 'Escape')
turtle.onkey(drunken_turtle, 'space')
turtle.listen()
turtle.mainloop()