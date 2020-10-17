def find_s():
    ls = [2]
    for i in range(3,100):
        flag = True
        for j in range(2,i-1):
            if i/j == i//j:
                flag = False
                break
        if flag:
            ls.append(i)

    return ls


ls = find_s()

def find_r(ls,a):
    for i in range(len(ls)):
        for j in range(i,len(ls)):
            if ls[i] + ls[j] == a:
                return str(a)+"="+str(ls[i])+"+"+str(ls[j])







k = 1
for i in range(6,101,2):
    if k == 5:
        print(find_r(ls,i),end = "\n")
        k = 1
    else:
        print(find_r(ls,i),end = ";")
        k = k+1

