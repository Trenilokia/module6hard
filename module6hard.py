from math import sqrt


class Figure:
    def __init__(self, color, sides):
        self.sides_count = 0
        self.__color = color
        self.sides = sides
        self.__sides = []
        self.filled = True

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color:
            self.__color = (r, g, b)

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True

    def get_sides(self):
        counter = []
        for i in range(self.sides_count):
            counter.append(self.sides)
        self.__sides = counter
        return self.__sides

    def __is_valid_sides(self, *sides):
        for side in sides:
            if not isinstance(sides, int):
                return False
            if sides <= 0:
                return False
            if side > self.sides_count:
                return False
        return True

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            if self.__is_valid_sides:
                side = new_sides[0]
                counter = []
                for i in range(self.sides_count):
                    counter.append(side)
                self.__sides = counter
                self.sides = side
        elif len(new_sides) > 1:
            pass


def __len__(self):
    return self.__sides


class Circle(Figure):
    def __init__(self, color, sides):
        Figure.__init__(self, color, sides)
        self.sides_count = 1
        self.__radius = sides / 2 * 3.14

    def get_radius(self):
        return self.__radius

    def get_square(self):
        return self.__radius * self.__radius * 3.14

    def __len__(self):
        return self.sides


class Triangle(Figure):
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.sides_count = 3

    def get_square(self):
        p = (self.sides * 3) / 2
        s = sqrt((p * (p - self.sides) * (p - self.sides) * (p - self.sides)))
        return s


class Cube(Figure):
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.sides_count = 12

    def get_volume(self):
        return self.sides ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
