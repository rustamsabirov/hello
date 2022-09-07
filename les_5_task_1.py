"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего
"""
import collections

company = collections.namedtuple('company', ['name', 'a1', 'a2', 'a3', 'a4', 'b'])
result = []
a = int(input("Введити кол-во компаний: "))
total = 0
for i in range(a):
    name = input(f"Название {i + 1}-ой компании: ")
    a1 = int(input("Прибыль за 1 квартал: "))
    a2 = int(input("Прибыль за 2 квартал: "))
    a3 = int(input("Прибыль за 3 квартал: "))
    a4 = int(input("Прибыль за 4 квартал: "))
    b = a1 + a2 + a3 + a4
    total += b
    result.append(company(name=name, a1=a1, a2=a2, a3=a3, a4=a4, b=b))
sr = total / a
print(f"Средняя прибыль компаний по базе: {sr}")
print(f"Компании с прибылью выше средней: ")
for company in result:
    if company.b >= sr:
        print(company.name)
print(f"Предприятия с прибылью ниже средней: ")
for company in result:
    if company.b < sr:
        print(company.name)