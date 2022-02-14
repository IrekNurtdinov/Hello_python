# 42. Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах

a = 1102223332555115
b= str(a)
count = 1
for i in range(len(b)-1):
    if i< len(b)-2 and b[i] == b[i+1]:
        count += 1
        c = (count,b[i])
    elif i == (len(b)-2) and b[i] == b[i+1]:
        count += 1
        c = (count,b[i])
        print(c)
    else: 
        c = (count,b[i])
        print(c)
        count = 1                 # последние элементы не выводит на печать

        

