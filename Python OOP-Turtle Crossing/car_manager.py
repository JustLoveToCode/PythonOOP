from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        # Creating the Attribute for the car:
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            # Instantiating the turtle class with the shape "square":
            # and passed into the variable new_car:
            new_car = Turtle("square")
            # Create the size of the car using the shapesize method:
            new_car.shapesize(stretch_wid=0.8, stretch_len=1.5)
            # Using the penup method to remove any line that is drawn:
            new_car.penup()
            # Using the turtle color method to create random color
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, +250)
            # goto is telling the car object to go to the random coordinate
            # on the y-axis coordinate:
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars_backward(self):
        for car in self.all_cars:
            # This will create the speed on the car
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
