from turtle import Turtle

class Snake:
    
    def __init__(self) -> None:
        self.segments = []
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.length = len(self.starting_positions)

        for index in range(0, self.length):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(self.starting_positions[index])
            self.segments.append(segment)
    
    def move(self):
        # This way our snake seems to have a solid one-piece body
        for seg_num in range(self.length - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(20)