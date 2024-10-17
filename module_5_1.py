class House:
    def __init__(self, name, number_of_floors):

        self.name = name
        self.number_of_floors = number_of_floors

        print(f'Объект {self.name}, количество этажей - {self.number_of_floors}')


    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(("Такого этажа не существует"))
        else:
            for i in range(1, new_floor+1):
                print(i)





h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h1.go_to(17)
h2.go_to(10)