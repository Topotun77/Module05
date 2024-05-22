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
        self.numberOfFloors = 10

    def go(self, floors_):
        """  Перемещение лифта  """
        attr_name = 'currentFloors'
        setattr(self, attr_name, floors_)
        # self.currentFloors = floors_


my_house = House()
print('Всего этажей в моем доме:', my_house.numberOfFloors)

for floors in range(0, my_house.numberOfFloors + 1, 2):
    my_house.go(floors)
    print(f'Текущий этаж равен: {my_house.currentFloors}')


