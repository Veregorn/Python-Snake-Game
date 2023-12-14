from turtle import Turtle
import random

# We can inherit this class from Turtle class so it has all the super class methods
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed("fastest") # I don't want to see the food moving to a new random position
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280) # So the food is completely inside the screen
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)