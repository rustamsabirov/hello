my_dict = {}
with open('learning.txt', 'r',encoding='utf-8') as my_var:
    for line in my_var:
        name, lect, pract, lab = line.split()
        my_dict[name] = int(lect) + int(pract) + int(lab)
    print(f'Общее количество часов по предмету: {my_dict}')
