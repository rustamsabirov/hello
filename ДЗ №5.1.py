with open('my_file.txt', 'w') as a_1:
    line=input('Введите текст: ')
    a_1.write(line+'\n')
    while line:
        line = input('Введите текст: ')
        a_1.writelines(line)
        if not line:
            break

with open('my_file.txt', 'r') as a_1:
    s_1=a_1.read()
    print(s_1)
