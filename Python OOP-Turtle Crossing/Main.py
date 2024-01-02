import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Creating the Message object:
# Instantiating the turtle object for writing the Message:
message = Turtle()
message.hideturtle()
message.penup()
message.goto(0, 0)

# Creating the screen object:
screen = Screen()
# Setting up the Screen for the width and height:
screen.setup(width=600, height=600)
screen.tracer(0)

# Instantiating the Player class:
player = Player()
# Instantiating the CarManager class:
car_manager = CarManager()
# Listen for Any Events on the Screen especially Keystroke:
screen.listen()

# Instantiating the ScoreBoard Class:
scoreboard = Scoreboard()

# Key for Going Upward:
screen.onkey(player.go_up, "Up")

# Key for Going Downward:
screen.onkey(player.go_down, "Down")

# Key for Going Left:
screen.onkey(player.go_left, "Left")

screen.onkey(player.go_right, "Right")

# Setting the game_is_on is True:
game_is_on = True

# While this is True:
while game_is_on:
    # Going to refresh every 0.3s:
    time.sleep(0.2)
    screen.update()
    # Invoking the method for create_car():
    car_manager.create_car()
    # Invoking the method for move_cars_backward():
    car_manager.move_cars_backward()

    # Detect collision with the car:
    for car in car_manager.all_cars:
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.increase_speed()
            scoreboard.increase_level()

        # If the player is 20 pixels or LESS as compared to the
        # centre of the car: Measuring the Center of the turtle to the center of the car:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
