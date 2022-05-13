from turtle import Turtle
from player import WIDTH, HEIGHT
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_X = range(round(WIDTH/2), round(3 * WIDTH / 2) + 1, 10)
STARTING_Y = range(round(-HEIGHT/2) + 80, round(HEIGHT/2) - 59, 20)
STARTING_SPEED = 1
SPEED_INCREASE = 1
CAR_VARIANCE = range(-25, 26, 1)

DIFFICULTY = 25


class Car(Turtle):

    def __init__(self):
        super(Car, self).__init__()
        self.shape("square")
        self.setheading(180)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(random.choice(STARTING_X), random.choice(STARTING_Y))
        self.move_speed = STARTING_SPEED

    def drive(self):
        self.forward(self.move_speed)

    def increase_speed(self):
        self.move_speed += SPEED_INCREASE


class CarManager:

    def __init__(self):
        self.cars = []
        for i in range(DIFFICULTY):
            self.cars.append(Car())

    def drive_all_cars(self):
        for car in self.cars:
            car.drive()

    def wrap_around_cars(self):
        for car in self.cars:
            if car.xcor() < -WIDTH/2 - 25:
                car.color(random.choice(COLORS))
                car.goto(WIDTH/2 + 45 - random.choice(CAR_VARIANCE), random.choice(STARTING_Y))

    def speed_up_cars(self):
        for car in self.cars:
            car.increase_speed()

    def crash_detected(self, player):
        for car in self.cars:
            if player.distance(car) < 20:
                return True
        return False
