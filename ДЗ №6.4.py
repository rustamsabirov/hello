"""
6.4 Реализуйте базовый класс Car. У данного класса должны быть
следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
PoliceCar. Добавьте в базовый класс метод show_speed, который
должен показывать текущую скорость автомобиля. Для классов TownCar
и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехал(а)'

    def stop(self):
        return f'{self.name} остановился(лась)'

    def turn_right(self):
        return f'{self.name} повернул направо'

    def turn_left(self):
        return f'{self.name} повернул налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} - {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} превышает допустимую для городских автомобилей'
        else:
            return f'Скорость {self.name} в пределах нормы для городских автомобилей'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочего автомобиля {self.name} - {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} превышает допустимую для рабочих автомобилей'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейская машина'
        else:
            return f'{self.name} не относится к полицейским'

bugati = SportCar(100, 'Желтая', 'Бугати', False)
matiz = TownCar(30, 'Синий', 'Матиз', False)
uaz = WorkCar(70, 'Коричневый', 'УАЗ', False)
opel = PoliceCar(110, 'Голубой',  'Опель', True)
print(uaz.turn_left())
print(f'{matiz.turn_right()}, а {bugati.stop()}')
print(f'{uaz.go()}, {uaz.show_speed()}')
print(f'{uaz.name} - {uaz.color}')
print(f'{bugati.name} полицейская машина? {bugati.is_police}')
print(f'{matiz.name}  полицейская машина? {uaz.is_police}')
print(bugati.show_speed())
print(matiz.show_speed())
print(opel.police())
print(opel.show_speed())