# 14. Найти третью цифру числа или сообщить, что её нет

import random
a = random.randint(-1000,1000)
print(a)
b = abs(a)
if b in range(100,1000):
    print(b%10)
else:
    print(f'Третьей цифры у числа {a} нет')