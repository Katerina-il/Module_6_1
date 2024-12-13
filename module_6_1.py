""" Домашнее задание по теме "Зачем нужно наследование"

Задача "Съедобное, несъедобное":

Разнообразие животного мира давно будоражит умы человечества. Царства, классы, виды... Почему бы и нам не попробовать выстроить что-то подобное используя наследования классов?
Необходимо описать пример иерархии животного мира, используя классы и принцип наследования.
Создайте:
2 класса родителя: Animal, Plant
Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.
Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения
4 класса наследника:
Mammal, Predator для Animal.
Flower, Fruit для Plant.  """
# from symtable import Class

class Animal:
    alive = True # (живой) атрибуты
    fed = False # (накормленный)

    def __init__(self, name):
        self.name = name # индивидуальное имя

    def eat(self, food):
        if isinstance(food, Fruit) and food.edible == True:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Plant:
    edible = False # (съедобность)

    def __init__(self, name):
        self.name = name # индивидуальное имя

class Mammal (Animal):

    def eat(self, food):
        if isinstance(food, Fruit) and food.edible == True:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        if food.edible == False:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Predator(Animal):
    pass

class Flower (Plant):
    pass

class Fruit (Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')



print(a1.name) # Волк с Уолл-Стрит не стал есть Цветик семицветик
print(p1.name) # Цветик семицветик
print(a1.alive) # живой волк
print(a2.fed) # ненакормленный Хатико
a1.eat(p1) # Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)  # Хатико съел Заводной апельсин
print(a1.alive) # жив ли Волк? - нет
print(a2.fed) # накормлен ли Хатико? - да