# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

# solved


def multN(N):
    mult = 1
    list = []
    for i in range(1, N+1):
        mult = mult*i
        list.append(mult)
    return list

print(multN(5))
