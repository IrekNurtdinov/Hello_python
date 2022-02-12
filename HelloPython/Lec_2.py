# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') #создать новый файл/добавить запись в существующий файл
# data = open('file.txt', 'w') #перезаписать данный в файл

# data.writelines(colors)  # разделителей не будет
# data.write('Line 20\n')
# data.write('Line 30\n')
# data.close()

# with open('file2.txt','w') as data:
#     data.write('Line 20\n')
#     data.write('Line 30\n')     #здесь можно без data.close

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()



# from hello import f 
# print(f(1))

# def new_string(symbol,count):
#     return symbol*count
# # print(new_string('!', 5))  #  !!!!!
# # print(new_string('!'))  #  Type error


# def new_string(symbol,count=3):
#     return symbol*count
# print(new_string('!', 5))  #  !!!!!    
# print(new_string('!')) #!!!
# print(new_string(4))  # 12

# def concatenation(*params):
#     res: str = ""                   #все как строки
#     for item in params:
#         res += item
#     return res

# print(concatenation('a', 's', 'd', 'f'))  # asdf
# print(concatenation('a', '1', 'd', '2'))  # a1d2
# print(concatenation(1,2,3,4))  # TypeErro

# def concatenation(*params):
#     res = 0                   #если только с числами
#     for item in params:
#         res += item
#     return res

# print(concatenation(1,2,3,4))    


##                 РЕКУРСИЯ

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


# list = []
# for e in range (1,10):
#     list.append(fib(e))
# print(list)


##          КОРТЕЖИ

# a = (3,4,41,4)  # кортеж - это неищзменяемый список
# print(a)
# print(a[0])
# print(a[-2])

# a = (3,4,5)
# for item in a:
#     print(item)

# t = ()
# print(type(t))  #tuple

# t = (1,)
# print(type(t))    #tuple

# t = (1)
# print(type(t))     # int

# t = (28,9,1990)
# print(type(t))

# colors = ['red', 'green', 'blue']
# print(colors)
# t = tuple(colors)
# print(t)



#        СЛОВАРИ

dictionary = {}
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }

# print(dictionary)
# print(dictionary['left'])

# for k in dictionary.keys():
#     print(k)

# for k in dictionary.values():
#     print(k)  

# for k in dictionary:
#     print(dictionary[k])

# dictionary['up'] = 'up'
# print(dictionary['up'])




#            МНОЖЕСТВА

# colors = {'red', 'green', 'blue'}
# print(type(colors))  # set

# colors.add('red')  # не добавляет то, что уже есть
# print(colors)

# colors.add('gray')  #  добавляет 
# print(colors)

# colors.remove('red')  #  удаляет
# print(colors)

# colors.remove('gray') # ошибка при удалении того чего нет
# print(colors)

# colors.discard('gray') # не удалет чнгго нет и ошибки не выдает
# print(colors)

# colors.clear()    # очищает множество set()
# print(colors)


# a = {1,2,3,5,8}
# b = {2,5,8,13,21}   
# c = a.copy() #копирует множество
# u = a.union(b)    # объединение множеств
# print(u)
# i = a.intersection(b) # пересечение
# print(i)

# dl = a.difference(b)  # вычитание b из а   dl = {1,3}
# print(dl)
# dr = b.difference(a)     # вычитание а из b   dr = {13,21}
# print(dr)    .

# q = a \
#     .union(b)\
#     .difference(a.intersection())  
# print(q)

# s = frozenset(a)  # превращаем в неизменяемое множество




#     СПИСКИ

# list1 = [1,2,3,4,5]
# list2 = list1

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# list1[0] = 123
# list2[1] = 333

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)


list1 = [1,2,3,4,5]
# print(list1)
# print(list1.pop()) # удаляет послений элемент
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

# list1.pop(2) # удаляет элемент с индексом 2
# print(list1)

# list1.insert(2, 11) # вставляем элемент 11 в позицию с индексом 2
# print(list1)

list1.append(11)  # добавление элемента в конец
print(list1)