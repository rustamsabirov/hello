"""
2. Представлен список чисел.
Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
"""
result=[]
my_list=[int(a) for a in input('Введите список чисел: ').split()]
for a in range(1,len(my_list)):
    if my_list[a]>my_list[a-1]:
        result.append(my_list[a])
print('Исходный список: ', my_list)
print('Список с элементами больше предыдущего: ', result)
