# 34. Написать программу замену элементов массива на противоположные

list = [25, 2, -65, 7, -2, 0]

for i in range(0,len(list)):
    list[i] = -list[i]
print(list)