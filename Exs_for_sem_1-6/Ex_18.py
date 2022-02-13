# 18. Реализовать алгоритм перемешивания списка. 
# решено

import random 
list = [1,2,3,4,5,6]
for i in range(0,len(list)-1):
    n= random.randint(i+1,len(list)-1)
    a = list[i]
    list[i] = list[n]
    list[n] = a

print(list)
