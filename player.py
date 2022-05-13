from turtle import Turtle
HEIGHT = 600
WIDTH = 600
PLAYER_MOVE_DIST = 10
STARTING_POS = (0, -HEIGHT/2 + 40)


class Player(Turtle):

    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_pos()

    def move_forward(self):
        self.forward(PLAYER_MOVE_DIST)

    def move_backward(self):
        if self.ycor() > -HEIGHT/2 + 20:
            self.back(PLAYER_MOVE_DIST)

    def reset_pos(self):
        self.goto(STARTING_POS)
