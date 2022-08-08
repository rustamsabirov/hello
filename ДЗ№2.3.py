my_dict={1:'зима',2:'весна',3:'лето',4:'осень'}
my_list=['зима','весна','лето','осень']
try:
    month=int(input('Пользователь введите № месяца от 1 до 12: '))

    if month==12 or month==1 or month==2:
        print(my_dict.get(1))
        print(my_list[0])
    elif month==3 or month==4 or month==5:
        print(my_dict.get(2))
        print(my_list[1])
    elif month==6 or month==7 or month==8:
        print(my_dict.get(3))
        print(my_list[2])
    elif month==9 or month==10 or month==11:
        print(my_dict.get(4))
        print(my_list[3])
    else:
        print('Такого месяца нет')
except ValueError:
    print('Ошибка ввода')
