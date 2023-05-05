from turtle import Turtle


class Field(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.sety(-200)
        self.make_field()
        self.hideturtle()

    def make_field(self):
        for move in range(4):
            self.penup()
            self.goto(-300, self.ycor() + 100)
            for street_lane in range(20):
                self.pendown()
                self.forward(20)
                self.penup()
                self.forward(10)
