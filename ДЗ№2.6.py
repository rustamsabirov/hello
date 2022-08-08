# Структуру данных «Товары»

my_dict = []
my_list = []

try:
    position = int(input("Введите количество товара: "))
    number = 1
    while number <= position:
        my_dict = dict({'название': input('Введите название: '), 'цена': input('Введите цену: '),
                        'количество': input('Введите количество: '), 'eд': input('Введите единицу измерения: ')})
        my_list.append((number, my_dict))
        number += 1
    print('_________________________')
    print('Структуру данных «Товары»:')
    print(my_list)

# Модуль аналитика «Товары»
    name, price, quantity, edenica = [], [], [], []
    for el in my_list:
        inf=el[1]
        for key,val in inf.items():
            if key=='название':
                name.append(val)
            elif key=='цена':
                price.append(val)
            elif key=='количество':
                quantity.append(val)
            else:
                edenica.append(val)
        my_analys={'название товаров':name, 'цена товаров':price, 'количество товаров':quantity, 'еденица количества товаров':edenica}
    print('_________________________')
    print('Аналитика по товарам:')
    print(my_analys)
except ValueError:
    print('Ошибка ввода, будьте внимательны')