# 16. Дано число обозначающее день недели. Выяснить является номер дня недели выходным

a = int(input('Введите число от 1 до 7: '))
if a in range(1,6):
    print('Рабочий день')
elif a in range (6,8):
    print('Выходной')
else:
    print('Попробуй еще раз')