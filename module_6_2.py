#Задача "Изменять нельзя получать"

class Vehicle():
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    owner = ''
    __model = ''
    __engine_power = 0
    __color = ''


    def __init__(self, owner, model, color,engine_power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power



    def get_model(self) -> str:
        return f' Модель {self.__model}'

    def get_horsepower(self) -> int:
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self) -> str:
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'Модель: {self.__model}')
        print(f'Мощность двигателя: {self.__engine_power}')
        print(f'Цвет: {self.__color}')
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя изменить цвет на {new_color}')

class Sedan(Vehicle):
    __model = "Sedan"
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
