def delenie(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
print(delenie(int(input('Введите 1-ый аргумент: ')),int(input('Введите 2 аргумент: '))))


