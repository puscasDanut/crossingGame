from turtle import Turtle, Screen
import turtle
from random import randint, choice


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Diffuiculty Selector")
screen.bgcolor('gray')
difficulty = screen.textinput("Difficuly", "Do you want hard or easy mode?")

if difficulty == 'easy':
    STARTING_MOVE_DISTANCE = 5
    MOVE_INCREMENT = 10
elif difficulty == 'hard':
    STARTING_MOVE_DISTANCE = 10
    MOVE_INCREMENT = 15

def random_position():
    return randint(-80, 180)


def random_color():
    return choice(COLORS)


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.car_list = []
        self.hideturtle()

    def move(self):
        for car in self.car_list:
            car.forward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

    def create_car(self):
        new_car = Turtle()
        new_car.shape('square')
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random_color())
        new_car.goto(300, random_position())
        new_car.setheading(180)
        self.car_list.append(new_car)

    def delete_cars(self):
        for car in self.car_list:
            car.hideturtle()

    def remove_car(self, car):
        if car.xcor() < -300:
            self.car_list.remove(car)
            car.hideturtle()
