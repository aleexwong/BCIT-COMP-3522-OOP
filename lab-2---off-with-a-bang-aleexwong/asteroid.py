import math
from vector import Vector
import random


class Asteroid:
    """
    id of the Asteroid
    """
    id = 0
    """
    min radius 
    """
    MIN_RADIUS = 1
    """
    max radius 
    """
    MAX_RADIUS = 4
    """
    max position
    """
    MAX_POSITION = 100
    """
    min position
    """
    MIN_POSITION = 0
    """
    max velocity
    """
    MAX_VELOCITY = 5
    """
    min velocity
    """
    MIN_VELOCITY = -5

    def __init__(self, radius, position, velocity):
        """
        Initialize the asteroid circumference in metres , position , velocity
        :param radius: an int
        :param position: a vector with x , y , z
        :param velocity: a vector with x , y , z
        """
        self.radius = 2 * math.pi * radius
        self.position = position
        self.velocity = velocity
        self.id = Asteroid.add_id()

    @classmethod
    def add_id(cls):
        """
        :return: add 1 to id of new asteroid
        """
        cls.id += 1
        return cls.id

    @classmethod
    def random_radius(cls):
        """
        :return: random radius for x y z
        """
        return random.randint(cls.MIN_RADIUS, cls.MAX_RADIUS)

    @classmethod
    def random_position(cls):
        """
        :return: random position for x y z
        """
        return Vector(random.randint(cls.MIN_POSITION, cls.MAX_POSITION),
                      random.randint(cls.MIN_POSITION, cls.MAX_POSITION),
                      random.randint(cls.MIN_POSITION, cls.MAX_POSITION))

    @classmethod
    def random_velocity(cls):
        """
        :return: random velocity for x y z
        """
        return Vector(random.randint(cls.MIN_VELOCITY, cls.MAX_VELOCITY),
                      random.randint(cls.MIN_VELOCITY, cls.MAX_VELOCITY),
                      random.randint(cls.MIN_VELOCITY, cls.MAX_VELOCITY))

    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def set_velocity(self, velocity):
        self.velocity = velocity

    def get_velocity(self):
        return self.velocity

    def move(self):
        self.position.add(self.velocity)
        return self.position

    def asteroid(self):
        return f"Asteroid: {self.id}, " \
               f"Position: {self.position}, " \
               f"Velocity {self.velocity}, " \
               f"Circumference {self.radius}"

    def __str__(self):
        return f"{self.asteroid()}"


def main():
    """
    Drives the Program.
    """
    vectorpos = Vector(0, 0, 0)
    vectorvel = Vector(1, 1, 1)
    asteroid = Asteroid(10, vectorpos, vectorvel)
    vectorpos.add(vectorvel)
    asteroid.set_velocity(vectorpos)
    print(f"{asteroid.__str__()}")
    print(asteroid.move())


if __name__ == '__main__':
    main()
