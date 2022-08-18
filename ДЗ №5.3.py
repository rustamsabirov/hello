try:
    with open('sotr.txt', 'r', encoding='UTF-8') as a_1:
        my_surname = []
        my_oklad = []
        my_list = a_1.read().split('\n')
        for i in my_list:
            i = i.split()
            if float(i[1]) < 20000:
                my_surname.append(i[0])
            my_oklad.append(i[1])
    sr_oklad=round(sum(map(float,my_oklad))/len(my_oklad))
    print(f'Сотрудники с окладом меньше 20.000: {my_surname}, средний оклад: {sr_oklad}')
except FileNotFoundError:
    print('Список sotr.txt не найден')
