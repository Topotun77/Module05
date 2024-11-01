# Домашнее задание по уроку "Перегрузка операторов"
#
# Создайте новый проект в PyCharm
# Запустите созданный проект
# Ваша задача:
# Создайте новый класс Buiding
# Создайте инициализатор для класса Buiding, который будет задавать целочисленный
# атрибут этажности self.numberOfFloors и строковый атрибут self.buildingType
# Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType
# для сравнения
# Полученный код напишите в ответ к домашему заданию
from random import choice


class Buiding:
    def __init__(self, name='Объект'):
        """  Инициализация объекта класса  """
        self.name = name
        self.numberOfFloors = 16
        self.buildingType = choice(['кирпичное', 'панельное', 'каменное', 'бревенчатое', 'из соломы'])

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

    def __str__(self):
        """  Вывод всех атрибутов объекта
          Не по заданию, а просто в качестве эксперимента
          Можно не проверять
          Понимаю, что некрасиво и нечитаемо, но все равно работает так как задумывалось )
        """

        # return str(self.__dict__)    эта строка тоже работает, но хотелось переписать по-своему

        list_ = list(map(lambda x, y: '\t' + str(x) + ' = ' + str(y) + '\n', self.__dict__.keys(),
                         self.__dict__.values()))
        return f'Атрибуты объекта "{self.name}":\n' + ' '.join(list_)


my_buid_1 = Buiding()
my_buid_2 = Buiding('Объект №2')

print(my_buid_1)
print(my_buid_2)

if my_buid_1 == my_buid_2:
    print('Оба объекта одинаковые')
else:
    print('Объекты разные')
