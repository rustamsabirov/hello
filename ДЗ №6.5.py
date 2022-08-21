'''
6.5. Реализовать класс Stationery (канцелярская принадлежность).
   определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
   создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
   в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
   создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

'''

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'Запуск отрисовки'

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} приставил(а) крестик'

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} сделал зарисовку'

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} обозначил контур'
station=Stationery(' ')
pen = Pen('Синяя ручка')
pencil = Pencil('Красный карандаш')
handle = Handle('Черный маркер')
print(station.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())