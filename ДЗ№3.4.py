def my_func (x,y):
    return x**y

def my_func_2 (x,y):
    counter=1
    z=1/x
    while counter < abs(y):
        z=z*1/x
        counter+=1
    return z

print(f'Первый вариант реализации: ',
    my_func(int(input('Введите число-основание "x": ')),int(input('Введите число-степень "y": ')))
)

print(f'Второй вариант реализации: ',
    my_func(int(input('Введите число-основание "x": ')),int(input('Введите число-степень "y": ')))
)