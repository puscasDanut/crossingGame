import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from field import Field
from random import randint

if __name__ == '__main__':
    def game():
        screen = Screen()
        screen.setup(width=600, height=600)
        screen.tracer(0)
        screen.bgcolor('gray')
        screen.title("Danut Crossing game")

        field = Field()
        player = Player()
        cars = CarManager()
        score = Scoreboard()

        screen.listen()
        screen.onkeypress(key="w", fun=player.move)

        def generate_car():
            difficulty = score.level
            random_int = randint(0, 10)
            if random_int > 10 - difficulty:
                cars.create_car()

        game_over = False
        while not game_over:
            time.sleep(0.1)
            screen.update()
            if player.check_if_won():
                player.reset_position()
                score.increase_score()
                cars.increase_speed()
                cars.delete_cars()
            generate_car()
            for car in cars.car_list:
                if abs(car.xcor() - player.xcor()) < 25 and abs(car.ycor() - player.ycor()) < 20:
                    screen.clear()
                    screen.bgcolor('gray')
                    score.game_over()
                    time.sleep(1)
                    play_again = screen.textinput("Play again", "Do you want to play again? (no/yes)")
                    if play_again == 'yes':
                        screen.clear()
                        game()
                    screen.exitonclick()
                cars.remove_car(car)
            cars.move()


    game()

# yeah fam
