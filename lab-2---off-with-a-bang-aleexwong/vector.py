class Vector:

    def __init__(self, x, y, z):
        """
        :param x: position x
        :param y: position y
        :param z: position z
        """
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        """
        :return: x cord
        """
        return self._x

    def get_y(self):
        """
        :return: y cord
        """
        return self._y

    def get_z(self):
        """
        :return: z cord
        """
        return self._z

    def add(self, vector):
        """
        :param vector:
        :return: x y z cords
        """
        self._x += vector.get_x()
        self._y += vector.get_y()
        self._z += vector.get_z()

    def tuple(self):
        """
        :return: x y z as a tuple
        """
        return self._x, self._y, self._z

    def __str__(self):
        """
        :return: format tuple
        """
        return f"{self.tuple()}"


def main():
    """
    Drives the Program.
    """
    vectest = Vector(0, 0, 0)
    vectest2 = Vector(1, 2, 1)
    print(f"Before: {vectest}")
    vectest.add(vectest2)
    print(f"After: {vectest}")


if __name__ == '__main__':
    main()
