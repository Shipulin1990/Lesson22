class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (self.name, self.number_of_floors)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(str(f'Название: {h1.name}, кол-во этажей: {h1.number_of_floors}'))
print(str(f'Название: {h2.name}, кол-во этажей: {h2.number_of_floors}'))
print(len(h1))
print(len(h2))
