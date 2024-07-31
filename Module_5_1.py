class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if new_floor > self.number_of_floors or new_floor < 1:
                print('Такого этажа не существует')
                break
            if i <= new_floor:
                print(i)


h1 = House('ЖК Эльбрус', 30)
h2 = House('ЖК Горский', 22)
h3 = House('ЖК Домик в деревне', 2)

print(h1.name, h1.number_of_floors)
print(h2.name, h2.number_of_floors)
print(h3.name, h3.number_of_floors)

h1.go_to(5)
h2.go_to(23)
h3.go_to(3)
