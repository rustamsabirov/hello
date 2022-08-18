with open('my_file.txt', 'r') as a_1:
    s_1=a_1.readlines()
    print(f'Количество строк в файле: {len(s_1)}')
    for i in range(len(s_1)):
        c_1 = s_1[i].split()
        print(f'В {i+1}-ой строке {len(c_1)} слов(а)')
