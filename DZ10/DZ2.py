# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое
# название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
# одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут
# быть обычные числа: V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать
# формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом
# уроке знания. Реализовать абстрактные классы для основных классов проекта и
# проверить работу декоратора @property.
from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def setV(self):
        pass

    @abstractmethod
    def setH(self):
        pass

    @abstractmethod
    def calculation(self):
        pass


class Clothes(MyAbstractClass):
    def __init__(self, name, type_clothes):
        self.name = name
        self.type_clothes = type_clothes

    def setV(self):
        pass

    def setH(self):
        pass

    def calculation(self):
        pass


class Coat(Clothes):
    def __init__(self, name, type_clothes, v):
        super().__init__(name, type_clothes)
        self.v = v

    @property
    def calculation(self):
        return round((self.v / 6.5 + 0.5), 2)


class Costume(Clothes):
    def __init__(self, name, type_clothes, h):
        super().__init__(name, type_clothes)
        self.h = h

    @property
    def calculation(self):
        return 2 * self.h + 0.3


coat = Coat('какое-то пальто:', 'пальто', 12)
costume = Costume('какой-то кастюм:', 'костюм', 2)
print('Расхода ткани для пальто:', coat.calculation)
print('Расхода ткани для костюма:', costume.calculation)
print('Общий расход ткани для пальто и костюма:', coat.calculation + costume.calculation)
