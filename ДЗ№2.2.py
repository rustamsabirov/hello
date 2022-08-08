my_list=[]
element_count=int(input('Введите количество элементов списка: '))

i=0

while i<element_count:
    my_list.append(input('Введите элемент списка: '))
    i+=1
print('Исходный список: ', my_list)

elem=0

for el in range(int(len(my_list)/2)):
    my_list[elem],my_list[elem+1]=my_list[elem+1],my_list[elem]
    elem+=2

print('Измененный список: ',my_list)

