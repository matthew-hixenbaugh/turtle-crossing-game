from turtle import Turtle
from player import WIDTH, HEIGHT
ALIGNMENT = 'center'
FONT = ("Courier", 20, "normal")
BIG_FONT = ("Courier", 36, "normal")


class LevelManager(Turtle):

    def __init__(self):
        super(LevelManager, self).__init__()
        self.hideturtle()
        self.current_level = 0
        self.goto(-WIDTH/2 + 80, HEIGHT/2 - 40)
        self.next_level()

    def next_level(self):
        self.current_level += 1
        self.clear()
        self.write(f"Level: {self.current_level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=BIG_FONT)
