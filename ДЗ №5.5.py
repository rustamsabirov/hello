try:
    with open('file.txt', 'r+') as file:
        my_numb = input('Введите цифры через пробел: ')
        file.writelines(my_numb)
        res = my_numb.split()
        print('Сумма чисел: ', sum(map(float,res)))
except ValueError:
    print('Ошибка ввода - необходимо вводить только числа!')
