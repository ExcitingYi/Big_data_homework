'''4.编制一个可以在命令行模式下运行的扫雷游戏。
    1)利用随机数进行布雷；
    2)计算无雷格子的邻居中包含地雷的数目；
    3)能够输入行号和列号表示要打开的格子；
    4)能够进行成片的展开。
'''
import random
def judge_end(ls):
    flag = True
    for i in range(1,len(ls)-1):
        for j in range(1,len(ls)-1):
            if ls[i][j] != "@" and ls_flag[i][j] == False:
                flag = False
                return flag
    return flag

def judge(ls,a,b):
    sum = 0
    if ls[a-1][b-1] == "@":
        sum = sum + 1
    if ls[a-1][b] == "@":
        sum += 1
    if ls[a-1][b+1] == "@":
        sum += 1
    if ls[a][b-1] == "@":
        sum += 1
    if ls[a][b+1] == "@":
        sum += 1
    if ls[a+1][b-1] == "@":
        sum += 1
    if ls[a+1][b] == "@":
        sum += 1
    if ls[a+1][b+1] == "@":
        sum += 1
    return sum

def creat():
    n = eval(input("请输入雷区大小n*n："))
    m = eval(input("请输入炸弹的个数m："))
    ls = []
    for i in range(n+2):
        ls.append([])
        for j in range(n+2):
            ls[i].append([])
    i = 0
    while(i < m):
        a = random.randint(1,n)
        b = random.randint(1,n)
        if ls[a][b] != "@":
            ls[a][b] = "@"
            i = i+1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if ls[i][j] != "@":
                ls[i][j] = judge(ls,i,j)
    for i in range(n+2):
        ls[0][i] = "#"
        ls[n+1][i] = "#"
        ls[i][0] = "#"
        ls[i][n+1] = "#"
    return ls
'''递归搜索'''
def find(ls,a,b):
    if ls[a][b] != 0:
        ls_flag[a][b] = True
    else:
        if ls_flag[a][b] == False:
            ls_flag[a][b] = True
            find(ls,a+1,b+1)
            find(ls,a+1,b)
            find(ls,a+1,b-1)
            find(ls,a,b+1)
            find(ls,a,b)
            find(ls,a,b-1)
            find(ls,a-1,b-1)
            find(ls,a-1,b)
            find(ls,a-1,b+1)

def display(ls):
    for i in range(1,len(ls)-1):
        for j in range(1,len(ls)-1):
            if ls_flag[i][j] == True:
                print("{:^4}".format(ls[i][j]),end = " ")
            else:
                print("{:^4}".format("[]"),end = " ")
        print("",end = "\n")

global ls_flag
ls_flag = []
ls = creat()
for i in range(len(ls)):
    ls_flag.append([])
    for j in range(len(ls)):
        ls_flag[i].append(False)

while(True):
    display(ls)
    n = input("请输入要打开的行号和列号，中间用空格分开:")
    n1 = int(n.split(" ")[0])
    n2 = int(n.split(" ")[1])
    if ls[n1][n2] == "@":
        for i in range(len(ls)):
            for j in range(len(ls)):
                if ls[i][j] == "@":
                    ls_flag[i][j] = True
        display(ls)
        print("踩雷，游戏结束。")
        break
    else:
        find(ls,n1,n2)
        if judge_end(ls):
            display(ls)
            print("恭喜您通关，游戏结束！")
            break