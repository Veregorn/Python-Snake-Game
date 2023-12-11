from turtle import Screen, Turtle

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Snake setup
turtles = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
length = 3

for index in range(0,length):
    turtle = Turtle(shape="square")
    turtle.color("white")
    turtle.goto(starting_positions[index])
    turtles.append(turtle)





screen.exitonclick()