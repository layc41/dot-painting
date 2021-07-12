import turtle as t
import random

color_list = [(132, 111, 102), (222, 230, 226), (222, 205, 119), (123, 90, 99),
              (202, 95, 76), (149, 161, 185), (81, 84, 130), (176, 147, 156),
              (154, 146, 87), (228, 172, 164), (148, 162, 150), (62, 23, 32),
              (178, 188, 214), (99, 113, 100), (179, 98, 107), (48, 47, 114),
              (224, 174, 181), (104, 40, 49), (136, 31, 25), (111, 118, 159),
              (40, 28, 74), (117, 137, 114), (96, 17, 11), (184, 196, 190),
              (80, 75, 40), (183, 196, 198)]

tim = t.Turtle()
tim.hideturtle()
t.colormode(255)
tim.speed("fastest")
tim.pensize(20)


def start():
    tim.penup()
    tim.goto(-225, -225)


def restart():
    tim.setheading(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)


def draw_spots():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)


start()
for _ in range(10):
    draw_spots()
    restart()


screen = t.Screen()
screen.exitonclick()