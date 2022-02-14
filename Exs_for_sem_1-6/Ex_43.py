# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
# решено

list = [1, 2, 3, 5, 1, 5, 3, 10,2,43,15]

def unic_list(a):
    new_list = []
    for i in a:
        if a.count(i) == 1:
            new_list.append(i)
    return new_list  



print(unic_list(list))
    