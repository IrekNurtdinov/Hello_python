# 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.
# решено

with open('Ex35.txt','r') as data:
    a = data.read()
    print(a)
    list = a.split(' ')
for i in range(1,len(list)):
    if int(list[i])-1 != int(list[i-1]):
        print(int(list[i])-1)


