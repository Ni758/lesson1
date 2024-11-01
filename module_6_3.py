
class Horse:

    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__()

    def run(self, dx):
        self.x_distance += dx

class Eagle:

    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'
        
    def fly(self, dy):
        self.y_distance += dy

class Unicorn(Horse, Eagle):  # Определение класса Unicorn, который наследуется от классов Horse и Eagle

    def move(self, dx, dy):  # Метод для перемещения unicorn
        super().run(dx)  # unicorn бежит на расстояние dx
        super().fly(dy)  # unicorn летит на расстояние dy

    def get_pos(self):  # Метод для получения текущей позиции unicorn
        return (self.x_distance, self.y_distance)  # Возвращает кортеж с текущими координатами unicorn

    def voice(self):  # Метод для вывода звука, который издает unicorn
        print(self.sound)  # Выводит звук, издаваемый unicorn


class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


# Пример работы программы:
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
