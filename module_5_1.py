class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'В доме "{self.name}" такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(f'Этаж: {floor}')







h1 = House('ЖК Байкал', 20)
h2 = House('Коттедж', 3)
h1.go_to(5)
h2.go_to(10)