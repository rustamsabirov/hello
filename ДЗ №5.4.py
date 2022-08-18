my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_str = []
try:
    with open('file.txt', 'r', encoding='utf-8') as file:
        with open('en_ru.txt', 'r+', encoding='utf-8') as en_ru:
            l = file.readlines()
            for i in l:
                i = i.split(' ', 1)
                my_str.append(my_dict[i[0]] + ' ' + i[1])
            en_ru.writelines(my_str)
except FileNotFoundError:
    print('Список не найден')
