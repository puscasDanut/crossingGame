from turtle import Turtle
import turtle

FONT = ("Courier", 24, "normal")
POSITION = (-175, 250)
GAME_OVER_FONT = ("Comic Sans", 50, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(POSITION)
        self.color('black')
        self.increase_score()
        self.hideturtle()

    def increase_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", font=FONT, align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", font=GAME_OVER_FONT, align="center")
        self.goto(0,-50)
        self.write(f"Final score: {self.level}", font=FONT, align="center")
