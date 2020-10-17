'''
2.为了提高小学生计算能力，现在需要为小学生编制计算题，要求如下：
   1)计算式中仅包含一个计算符号（加减乘除）和两个计算数；
   2)计算结果不能出现负数；
   3)一次需要出10个这样的题目。
'''

import random
for i in range(10):
    a = random.randint(1,100)
    b = random.randint(1,100)
    c = random.randint(1,4)
    if c == 1:
        print(str(a),"+",str(b),"=")
    elif c == 2:
        print(str(a),"/",str(b),"=")
    elif c == 3:
        print(str(a),"*",str(b),"=")
    else:
        if a - b > 0:
            print(str(a),"-",str(b),"=")
        else:
            print(str(b), "-", str(a), "=")