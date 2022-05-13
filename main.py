from turtle import Screen
from player import Player, HEIGHT, WIDTH
from carmanager import CarManager
from levelmanager import LevelManager
import time

FPS = 30


def main():
    screen = Screen()
    screen.setup(height=HEIGHT, width=WIDTH)
    screen.title("Turtle Crossing")
    screen.tracer(0)

    player = Player()
    car_manager = CarManager()
    level_manager = LevelManager()

    screen.listen()
    screen.onkeypress(player.move_forward, "w")
    screen.onkeypress(player.move_backward, "s")

    game_running = True
    while game_running:
        time.sleep(1/FPS)
        car_manager.drive_all_cars()
        screen.update()
        car_manager.wrap_around_cars()

        if player.ycor() >= HEIGHT/2 - 20:
            level_manager.next_level()
            car_manager.speed_up_cars()
            player.reset_pos()

        if car_manager.crash_detected(player):
            game_running = False
            level_manager.game_over()

    screen.exitonclick()


if __name__ == '__main__':
    main()
