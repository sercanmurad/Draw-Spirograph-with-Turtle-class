import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")
def draw_spirograph(size_of_gab):
  for _ in range(int(360/size_of_gab)):
    tim.color(random_color())
    tim.circle(100)
    current_heading=tim.heading()
    tim.setheading(current_heading+size_of_gab)

size=int(input("Please enter size gap!Please use numbers!"))
draw_spirograph(size_of_gab=size)
########### Challenge 5 - Spirograph ########






screen=t.Screen()
screen.exitonclick()