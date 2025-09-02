import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(10)

num_sides = 100
angle = 360 / num_sides

for i in range(num_sides):
    t.forward(10)
    t.left(angle)

screen.exitonclick()






