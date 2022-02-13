# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


list = [1, 2, 1, 5]
new_list = []
for i in range(0,len(list)-1):
    for j in range(i+1,len(list)):
        if list[i] == list[j]:
            list.pop(i)
            list.pop(j)

print(list)   
    