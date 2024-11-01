# Домашняя работа по уроку "Атрибуты и методы объекта."
# Домашнее задание по уроку "Пространство имен"
#
# Создайте новый проект в PyCharm
# Запустите созданный проект
# Ваша задача:
# Создайте новый класс House
# Задайте ему новый атрибут numberOfFloors = 10
# В цикле пройдитесь по атрибуту numberOfFloors и распечайте значение "Текущий этаж равен"
# Полученный код напишите в ответ к домашему заданию


# Менять в цикле атрибут numberOfFloors не стала, т.к. в моем понимании он определяет количество этажей в доме.
# Вместо него я ввела атрибут currentFloors, в который и записывается текущий этаж

class House:
    def __init__(self):
        """  Инициализация объекта класса  """
        from random import choice
        self.totalFloors = 16           # Всего этажей в доме
        self.type = choice(['кирпичный', 'панельный', 'соломенный', 'бревенчатый'])

    def go(self, floors_):
        """  Перемещение лифта  """
        attr_name = 'numberOfFloors'
        setattr(self, attr_name, floors_)
        # self.numberOfFloors = floors_


my_house = House()
my_house.numberOfFloors = 10            # Текущий этаж
print(my_house.__dict__)

print('Всего этажей в моем доме:', my_house.totalFloors)

for floors in range(my_house.numberOfFloors, 0, -1):
    my_house.go(floors)
    print(f'Текущий этаж равен: {my_house.numberOfFloors}')


