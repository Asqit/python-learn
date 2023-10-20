# Super()
# Super is a function used to access parent class attributes.
# It returns a temporary instance of a parent class when used


class Rect:
    # > pass

    # We added this constructor to reduce the code redundancy
    def __init__(self, width: int, length: int):
        self.width = width
        self.length = length


class Square(Rect):
    def __init__(self, length: int, width: int):
        # > self.width = width
        # > self.length = length

        # In order to get rid of this repeating code
        # we adjust the parent class via the super() function
        super().__init__(width, length)

    def area(self):
        return self.length * self.width


class Cube(Rect):
    def __init__(self, length: int, width: int, height: int):
        # > self.width = width
        # > self.length = length
        self.height = height

        # Just as we did in above class
        # we can use the super() function
        super().__init__(width, length)

    def volume(self):
        return self.length * self.width * self.height


square = Square(3, 3)
print(square.area())

cube = Cube(3, 3, 3)
print(cube.volume())
