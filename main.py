import turtle as t
import random

tim = t.Turtle()

num_sides = 7

my_colors = ["green", "yellow", "blue", "red", "pink", "purple"]


def shapes(num_sides):

    while num_sides > 0:
        angle = 360 / num_sides
        for _ in range(num_sides):
            tim.color(random.choice(my_colors))

            tim.forward(100)
            tim.right(angle)
        num_sides -= 1


shapes(num_sides)
