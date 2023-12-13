from turtle import Screen, Turtle
import time
import snake

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # Turn turtle animation off so we can decide when to update the screen

# Snake setup
snake = snake.Snake()

# Event Listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Snake movement
game_is_on = True

while game_is_on:
    screen.update() # So all the snake segments move together
    time.sleep(0.1) # So I can see how snake moves as slow as I want

    # Testing move
    snake.move()


screen.exitonclick()