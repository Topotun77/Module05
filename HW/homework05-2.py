# Домашняя работа по уроку "Специальные методы классов"
# Домашнее задание по уроку "Пространство имен"
#
# Создайте новый проект в PyCharm
# Запустите созданный проект
# Ваша задача:
# Создайте новый класс House
# Создайте инициализатор для класса House, который будет задавать атрибут этажности self.numberOfFloors = 0
# Создайте метод setNewNumberOfFloors(floors), который будет изменять атрибут numberOfFloors на параметр floors и выводить в консоль numberOfFloors
# Полученный код напишите в ответ к домашему заданию


# 2 первых метода для проверки по заданию, остальное просто эксперименты

from random import choice


class House:
    def __init__(self):
        """  Инициализация объекта класса  """
        self.numberOfFloors = 0
        self.type = choice(['кирпичный', 'панельный', 'соломенный', 'бревенчатый'])

    def setNewNumberOfFloors(self, floors):
        """  Изменение номера этажа  """
        self.numberOfFloors = floors
        print(f'Номер этажа: {floors}')

    def go(self, floors_):
        """  Перемещение лифта. Этот метод был описан в ДЗ №1 и остался здесь без вызова  """
        attr_name = 'numberOfFloors'
        setattr(self, attr_name, floors_)
        # self.numberOfFloors = floors_

    def __str__(self):
        """  Вывод всех атрибутов объекта
          Не по заданию, а просто в качестве эксперимента
          Можно не проверять
          Понимаю, что некрасиво и нечитаемо, но все равно работает так как задумывалось )
        """

        # return str(self.__dict__)    эта строка тоже работает, но хотелось переписать по-своему

        list_ = list(map(lambda x, y: '\t' + str(x) + ' = ' + str(y) + '\n', self.__dict__.keys(),
                         self.__dict__.values()))
        return f'Атрибуты объекта:\n' + ' '.join(list_)


my_house = House()
print(my_house)

my_house.setNewNumberOfFloors(choice([2, 6, 4, 7, 10, 33]))
