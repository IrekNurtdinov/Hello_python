# import random
# a = random.randint(2,22)
# print(a)

# a = eval('2+2')
# print(a)

import numpy as np
with open ('42.txt', 'r') as d:
    n = d.read()

n = list(map(int, n.split(',')))
print(n)
li = np.array([n])
unic_elements = np.unique(li)
print(unic_elements)
places_elements = np.unique(li, return_inverse = True)
print(places_elements)
print(li)
with open ('42_result.txt', 'w') as data:
    data.write(str(unic_elements))
