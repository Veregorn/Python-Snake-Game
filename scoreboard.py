from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(y=280)
        self.write('Score: {self.score}', align="center")

    def refresh_score(self):
        pass
    
    def increase_score(self):
        self.score += 1