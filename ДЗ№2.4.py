my_stroka=input('Пользователь введите предложение: ')
new_stroka=[]
number=1
try:
    for element in range(my_stroka.count(' ')+1):
        new_stroka=my_stroka.split()

        if len(str(new_stroka))<=10:
            print(f'{number} {new_stroka[element]}')
            number += 1
        else:
            print(f'{number} {new_stroka[element] [0:10]}')
            number += 1
except IndexError:
    print()