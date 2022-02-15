# 38. Напишите программу, удаляющую из текста все слова содержащие "абв".
# решено

a = 'абвапр рол абв рпавброол олрр роолд апрра прабвмит'
list = a.split(' ')
print(a)
str = 'абв'
new_list = []
for i in list:
    if not str in i:
        new_list.append(i)
b = ''        
for j in new_list:
    b += j + ' '
print(b)