# 16. Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму
# solved 


n = 3
list = []
sum = 0
for i in range(1, n+1):
    num = (1+1/i)**i
    list.append(num)
    sum += num
print(list)
print(sum)