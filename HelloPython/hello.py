# print ('hello world')

# ТИПЫ ДАННЫХ И ПЕРЕМЕННЫЕ
# int, float, boolean, str, list, None


# a = 123
# b = 1.23
# value = None  / если поока не знаем тип
# print (type(a))
# print (type (b))  / выводит тип переменной
# value = 12334
# print (type(value))
# print (a)
# print (b)

# s = 'hello world'

# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s))
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')  / интерполяция

# f = True
# print(f)

# list = [1, 2, 3]  / список (массив)

# list1 = ['1', '2', '3', 'hello', 1, 2, 4.5, True]
# print(list)
# print(list1)


# ВВОД И ВЫВОД ДАННЫХ

# print ('введите а')
# a = int(input())  /ввод с клавиатуры сразу целочисленного знака
# print ('введите b')
# b = int(input())
# print(a,' + ',b, ' = ', a+b)


# АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ

#  +, -, *, /, %, //, **
#

# a = 1.3
# b = 3
# c = a / b  # res in float
# c = a // b  # res in int
# c = a % b
# c = a**b
# c = round(a*b)
# c = round (a*b,3)   \ коичество цифр после запятой
# print(c)

# a = 5
# a +=3
# print(a)


# # ЛОГИЧЕСКИЕ ОПЕРАЦИИ
# >, >=, <, <=, ==, !=
#   not, and, or - не путать с &, |, ^
#  is, is not, in, not in


# a = 1 > 4
# a = 1< 4
# a = 1< 4 and 5 > 2
# a = 1 == 2
# a = 1 != 2
# print (a)

# a = 'qwe'
# b = 'qwe'
# print (a == b)

# a = [1,2]
# b = [1,2]
# print (a == b)

# a = 1<3<5  # тройное неравенство
# print (a)

# func = 1
# T = 4
# x = 123
# print (func<T>(x))

# f = 1>2 or 4<6
# print(f)

# f = [1,2,3,4]
# print (f)
# print (2 in f)
# print (not 2 in f)

# is_odd = f[0] % 2 == 0
# is_odd = not f[0] % 2
# print (is_odd)


#  УПРАВЛЯЮЩИЕ КОНСТРУКЦИИ IF, IF-ELSE, WHILE

#  if condition:       / отступы важны!!!
#  operator 1
#  operator 2
#  ...
#  operator n
# else:
# operator n+1
# operator n+2
# ...
# operator n+m


# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)


#  if condition1:
# operator
# elif condition2:
# operator
# elif condition3:
# operator
# else:
# operator


# username = input('Введите имя: ')
# if username == 'Маша':
#     print ('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)


#  while condition:       / отступы важны!!!
#  operator 1
#  operator 2
#  ...
#  operator n


# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print ('Пожалуй')
#     print ('хватит')
# print (inverted)



# for i in enumeration:
    #  operator 1
    #  operator 2
    #  ...
    #  operator n

# for i in 1,2,3,4,5:
#      print (i**2)


# list = [1,2,3,4,5]
# for i in list:
#     print(i**2)

# r = range(10)
# for i in r:
#     print(i)


# for i in range(10):
#     print(i)

# for i in range(1,5):
#     print(i)

# for i in range(1,10,2):    #шаг 2
#     print(i)

# for i in 'qwerty':    
#     print(i)



# РАБОТА СО СТРОКАМИ


from tkinter import N


text = 'съеШь ещё Этих мягких французских булок'
# help(str)
# print(len(text))  #39
# print('ещё' in text)   #True
# print(text.isdigit())   #False
# print(text.islower())   #True
# print(text.replace('ещё','ЕЩЁ'))
# print(text[0])
# print(text[len(text)-1])
# print(text[-5])
# print(text[:])
# print(text[:2])
# print(text[len(text)-2:])
# print(text[2:9])
# print(text[6:-18])
# print(text[0:len(text):2])
# print(text[::2])
# text = text[2:9] + text[-5] + text[::2]
# print(text)

# СПИСКИ

# numbers = [1,2,3,4,5]
# numbers = list(range(1,6))
# numbers[0] = 10
# print(numbers)

# for i in numbers:
#     i *=2
#     print(i)

# colors = ['red', 'green', 'blue']
# # for e in colors:
#     # print(e)

# # for e in colors:
# #     print(e*2)

# colors.append('gray')  #добавить в конец
# # print(colors)
# # print(colors== ['red', 'green', 'blue', 'gray'] )  #True
# # colors.remove('red')
# # colors.remove(colors[1])
# del colors[0]
# print(colors)

# ФУНКЦИИ

# def function_name(x):
#     body line 1
#     ..
#     body line n
#     optional return

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2
print(f(arg))





