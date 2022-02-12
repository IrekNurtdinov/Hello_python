# 13. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.


s1 = 'qwerthjkertjkerthjyoooertkkkj'
s2 = 'ert'

def counter(s1,s2):
    count = 0
    while len(s1):
        if s1.find(s2) != -1:
            index = s1.find(s2)
            s1 = s1[index+len(s2):]
            count += 1
            index = 0
        else:
            break
    return count

print(counter(s1,s2))