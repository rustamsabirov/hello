'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
 преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
 и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def abcd(cls, day_month_year):
        my_list = []

        for i in day_month_year.split():
            if i != '-':
                my_list.append(i)

        return int(my_list[0]), int(my_list[1]), int(my_list[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Правильная дата'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц (год)'
        else:
            return f'Неправильный день (месяц,год)'

    def __str__(self):
        return f'Текущая дата {Data.abcd(self.day_month_year)}'


# prov = Data('11 - 1 - 2001')
# print(prov)
first_data=Data.abcd('27 - 8 - 2022')
print(first_data )
print()
print(Data.valid(10, 8, 2021))
print(Data.valid(10, 12, 2040))
print(Data.valid(35, 12, 2040))
print(Data.valid(6, 13, 2020))


