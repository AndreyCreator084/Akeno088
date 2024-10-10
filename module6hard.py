from math import pi  # импортируем значение pi из модуля math

class Figure: # класс фигуры

    sides_count = 0

    def __init__(self, color, sides):  # конструктор фигуры с параметрами цвета и количества сторон фигуры
        self.__sides = sides
        self.__color = color
        self.filled = None

    def __len__(self): # возвращает периметр фигуры
        if self.sides_count == 0:
            return 0
        else:
            sum = 0
            for item in self.__sides:
                sum += item
            return sum

    def __is_valid_color(self, color): # проверка цвета фигуры
        for item in color:
            if not isinstance(item, int) or item < 1 or item > 255:
                return False
        return True

    def set_color(self, *new_color): # изменение цвета фигуры
        if self.__is_valid_color(new_color):
            self.__color = list(new_color)

    def get_color(self): # возвращает цвет фигуры
        return self.__color

    def __is_valid_sides(self, new_sides): # проверка сторон фигуры
        if self.sides_count != len(new_sides):
            return False

        for item in new_sides:
            if not isinstance(item , int):
                return False
        return True

    def set_sides(self, *new_sides): # изменение количества сторон фигуры
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

    def get_sides(self): # возвращает количество сторон фигуры
        return self.__sides


class Circle(Figure): # класс круга

    sides_count = 1

    def __init__(self, color, *sides): # конструктор круга с параметрами цвета и количества сторон круга
        if len(sides) != 1:
            sides = [1]
        super().__init__(color, sides)
        self.__radius = self.get_sides()[0] / (2 * pi) # радиус круга

    def get_square(self): # возвращает площадь круга
        return self.__radius ** 2 * pi

class Triangle(Figure): # класс треугольника

    sides_count = 3

    def __init__(self, color, *sides): # конструктор треугольника с параметрами цвета и количества сторон треугольника
        if len(sides) != 3:
            sides = [1] * 3
        super().__init__(color, sides)

    def get_square(self): # возвращает площадь треугольника
        sides = self.get_sides()
        p = (sides[0] + sides[1] + sides[2]) / 2
        return (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5

class Cube(Figure): # класс куба

    sides_count = 12

    def __init__(self, color, *sides): # конструктор куба с параметрами цвета и количества сторон куба
        if len(sides) != 1:
            sides = [1]
        sides = sides * 12
        super().__init__(color, sides)

    def get_volume(self): # возвращает объём куба
        return self.get_sides()[0] **3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

print('Проверка на изменение цветов:')
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

print('Проверка на изменение сторон:')
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

print('Проверка периметра (круга), это и есть длина:')
print(len(circle1))

print('Проверка объёма (куба):')
print(cube1.get_volume())
