# Name: Alex Wong
# Student number: A01889960

from datetime import datetime
from asteroid import Asteroid
import time

# 100 MAX
ASTEROIDS_MAX_NUMBER = 100

# REPEATER 3
TIME_THREE = 3


class Controller:

    def __init__(self, asteroid_id):
        """
        tracks and makes asteroids
        :param asteroid_id: an int.
        """
        self.list = []
        for i in range(asteroid_id):
            controller = Asteroid(Asteroid.random_radius(),
                                  Asteroid.random_position(),
                                  Asteroid.random_velocity())
            self.list.append(controller)

    def simulate(self, second):
        """
        simulation per second tracks 100 asteroids
        :param second: an int
        """

        print(f"Simulation Start Time {datetime.now()}\n"
              f"\nMoving Asteroids!"
              f"\n-----------------")
        nearest_second = datetime.now().microsecond
        time.sleep(((1000000 - nearest_second) / 1000000))

        for i in range(second):
            for asteroid in self.list:
                print(f"Asteroid {asteroid.id} Moved! Old Pos:"
                      f"{asteroid.move()} -> New Pos: {asteroid.move()}")
                print(f"Asteroid {asteroid.id} is currently at "
                      f"{asteroid.position} and moving at "
                      f"{asteroid.velocity} metres per second"
                      f" it has a circumference of {asteroid.radius}"
                      )
                time.sleep(1)


def main():
    """
    Drives the program.
    """
    controller = Controller(ASTEROIDS_MAX_NUMBER)
    controller.simulate(3)


if __name__ == '__main__':
    main()
