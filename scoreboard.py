from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.get_high_score())
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
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

        self.score = 0
        self.write_score()

    def get_high_score(self):
        high_score = ""
        
        with open("data.txt") as file:
            high_score = file.read()

        return high_score
    
    def save_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))