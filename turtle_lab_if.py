import turtle

while True:
    shape = input('Enter a shape:')
    if shape == 'circle':
        turtle.circle(50)
    elif shape == 'triangle':
        turtle.forward(50); turtle.left(120)
        turtle.forward(50);turtle.left(120)
        # 독립적인문장임을 위해 세미콜론을 넣어줌 
        turtle.forward(50)
    elif shape == 'quit':
        break
    else:
        print('Wrong Shape')

turtle.bye()