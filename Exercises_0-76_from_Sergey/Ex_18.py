# 18. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y
from operator import truediv


# x = True
# y = False

# print((not(x or y)) == (not x and not y))



# 2 вариант: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 

def logic(X, Y, Z):
    return not(X or Y or Z) == (not X and not Y and not Z)

for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            print(logic(x,y,z))