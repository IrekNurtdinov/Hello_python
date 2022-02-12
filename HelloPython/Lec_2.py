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




