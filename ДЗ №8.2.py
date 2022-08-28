'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
'''

class my_except:
    def __init__(self, info):
        self.info = info

    def delenie(*args):
        try:
            number_1=int(input('Введите делимое число: '))
            number_2=int(input('Введите делитель числа: '))
            if number_2==0:
                print( 'Делить на ноль нельзя!')
                exit()
            else:
                result=number_1/number_2
                return result
        except ValueError:
            return 'Ошибка ввода - необходимо вводит целые числа'

print(my_except.delenie())
