from turtle import Turtle
import turtle

turtle.addshape("broscoi.gif")
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("broscoi.gif")
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def check_if_won(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        return False

    def reset_position(self):
        self.goto(STARTING_POSITION)
