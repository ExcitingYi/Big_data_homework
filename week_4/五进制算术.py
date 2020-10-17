'''1.某种文明使用了五进制来表示数据，所使用的数字符号分为别：@、#、￥、%、&，请编写程序实现该文明的加法和除法。
要求：对输入的两个数字进行计算，数字的长度可能不等。
'''
def switch(a):
    if a == "@":
        return 0
    elif a == "#":
        return 1
    elif a == "$":
        return 2
    elif a == "%":
        return 3
    elif a == "&":
        return 4

def switch1(a):
    if a == 0:
        return "@"
    elif a == 1:
        return "#"
    elif a == 2:
        return "$"
    elif a == 3:
        return "%"
    elif a == 4:
        return "&"

def out(a):
    if a//5 != 0:
        return a%5 + 10 * out(a//5)
    else:
        return a

n1 = input("plz enter the first number:")
n2 = input("plz enter the sign:")
n3 = input("plz enter the second number:")
num1 = 0
num2 = 0
for i in n1:
    num1 = num1*5 + switch(i)

for i in n3:
    num2 = num2*5 + switch(i)

if n2 == "+":
    result = num1 + num2
elif n2 == "-":
    result = num1 - num2

fin = ""
for i in str(out(result)):
    fin = fin+switch1(int(i))

print(fin)