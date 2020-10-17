'''计算机中使用通配符’*’表示0个或若干个字符，现有主字符串mstr，和一个包含一个’*’的子字符串sstr，请编写程序查找sstr在mstr中是否存在。备注：本题中’*’不出现在sstr的首末两个位置。
'''
mstr = input("请输入原字符串：")
sstr = input("请输入子字符串：")

ls = sstr.split("*")
i = 0
flag = 0
while i < (len(mstr)):
    k = 0
    while k < len(ls[flag]) and i+k < len(mstr):
        if ls[flag][k] == mstr[i+k]:
            k = k+1
        else:
            break
    else:
        flag = flag + 1
        i = i + k - 1

    if flag == 2:
        break
    i = i + 1

if flag == 2:
    print("存在")
else:
    print("不存在")



