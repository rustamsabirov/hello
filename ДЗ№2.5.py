my_list=[7,5,3,3,2]
try:
    reiting=int(input('Введите новый номер рейтинга: '))
    my_list.append(reiting)
    print(sorted(my_list, reverse=True))
except ValueError:
    print('Ошибка ввода!')