# 14. Подсчитать сумму цифр в вещественном числе.
# решено
a = 1.1234

def get_sum(number):
    b = str(number)
    sum = 0
    for i in b:    
        if i != '.':
            sum += int(i)
    return sum
    
        
print(get_sum(a))

