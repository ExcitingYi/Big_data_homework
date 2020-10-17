import random
import math

ls = []

for i in range(1000000):
    x = random.uniform(2, 3)
    y = random.uniform(0, 20)
    if x**2 + 4*x*math.sin(x) > y:
        ls.append(1)
    else:
        ls.append(0)

sum = 0
for i in ls:
    sum = sum + i

print(sum/1000000 * 20)
