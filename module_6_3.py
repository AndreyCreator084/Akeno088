class Horse:

    def __init__(self):
        # Инициализация атрибутов класса Horse
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        # Метод для передвижения лошади на dx единиц
        self.x_distance += dx

class Eagle:

    def __init__(self):
        # Инициализация атрибутов класса Eagle
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        # Метод для передвижения орла на dy единиц
        self.y_distance += dy

class Pegasus(Horse, Eagle): # Наследование атрибутов классов Horse и Eagle

    def __init__(self):
        # Вызов методов __init__ классов Horse и Eagle
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        # Метод для передвижения Пегаса на dx и dy единиц
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        # Метод для получения текущей позиции Пегаса
        return (self.x_distance, self.y_distance)

    def voice(self):
        # Метод для вывода звука Пегаса
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
# Вывод текущей позиции Пегаса

p1.move(10, 15)
# Передвижение Пегаса на 10 единиц по горизонтали и 15 единиц по вертикали

print(p1.get_pos())
# Вывод новой текущей позиции Пегаса

p1.move(-5, 20)
# Передвижение Пегаса на -5 единиц по горизонтали и 20 единиц по вертикали

print(p1.get_pos())
# Вывод новой текущей позиции Пегаса

p1.voice()
# Вывод звука Пегаса



