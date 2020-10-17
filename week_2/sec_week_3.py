#只能分解质因数在1000以内的数。

def find_s():
    ls = [2]
    for i in range(3,1000):
        flag = True
        for j in range(2,i-1):
            if i/j == i//j:
                flag = False
                break
        if flag:
            ls.append(i)

    return ls

n = eval(input())
s = str(n)
ls = find_s()
print(ls)
yls = []

while (n != 1):
    for i in ls:
        if n/i == n//i:
            yls.append(str(i))
            n = n/i
            break

cout = ""
for i in range(len(yls)):
    cout = cout + "*" + yls[i]

print(s+"=" + cout[1:])