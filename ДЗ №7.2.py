'''
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
— одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих
типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod

class Odejda:

    def __init__(self, my_var):
        self.my_var = my_var

    @property
    def rasxod(self):
        return f'Всего затраченно ткани: {round(self.my_var / 6.5 + 0.5 + 2 * self.my_var + 0.3):}'

    @abstractmethod
    def abstract(self):
        return 'Абстрактный метод для одежды'


class Palto(Odejda):
    def rasxod(self):
        return f'Для пошива пальто нужно: {round(self.my_var / 6.5 + 0.5):} ткани'

    def abstract(self):
        return 'Абстрактный метод для пальто'


class Costume(Odejda):
    def rasxod(self):
        return f'Для пошива костюма нужно: {round(2 * self.my_var + 0.3): } ткани'

    def abstract(self):
        return 'Абстрактный метод для костюма'

itogo=Odejda(100)
palto = Palto(100)
costume = Costume(100)

print(palto.rasxod())
print(palto.abstract())

print(costume.rasxod())
print(costume.abstract())

print(itogo.rasxod)
print(itogo.abstract())
