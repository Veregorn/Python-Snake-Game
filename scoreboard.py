from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color("White")
        self.penup()
        self.goto(x=0, y=270)
        self.write_score()
    
    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    """ def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT) """
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.write_score()