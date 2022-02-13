# 17. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов 
# на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

# решено

import random


def Fill_list(N):     # создает список из N  элементов в диапазоне [-N,N] и записывает элементы в file3.txt построчно
    list = []
    while len(list) <= N-1:
        list.append(random.randint(-N,N))
        with open('file3.txt','w') as data:
            for i in list:
                data.writelines(str(i) + '\n')
    return list

print(Fill_list(5))

def mult_pos(a,b):                  # извлекает значения из file3.txt и вносит их в список, 
    with open('file3.txt','r') as data:           #далее перемножает значения на позициях  а и b
        list = []
        for line in data:
            list.append(line)
        mult = int(list[a-1])* int(list[b-1])
    return mult

print(mult_pos(3,5))    

