def jiami(a,b):
    return (4-len(str(a+1)))*"0"+str(a+1)+ (2-len(str((b+1)//20 + 1)))* "0" + str((b+1)//20 + 1) + (2-len(str((b%20 + 1))))*"0" + str((b%20 + 1))

fr = open("Three_country_txt.txt",'r',encoding = "utf-8")
#print(len(fr.readlines()))
w_set = set()
w_ls= [[]]
#整理，去掉标点，并将存在的文字存入w_set
count_ye = 0
count_zi = 0
for i in fr.readlines():    #读取，可能多行
    for j in i:
        w_set.add(j)
        w_ls[count_ye].append(j)
        count_zi += 1
        if count_zi == 400:     #翻页
            count_zi = 0
            count_ye += 1
            w_ls.append([])


w_dic = {}
#下为加密：
for ye in range(len(w_ls)):
    for zi in range(len(w_ls[ye])):       #每页400字
        if w_ls[ye][zi] in w_set:
            w_set.remove(w_ls[ye][zi])
            w_dic[w_ls[ye][zi]] = [jiami(ye,zi)]
        else:
            w_dic[w_ls[ye][zi]].append(jiami(ye,zi))

print("加密已完成。")
print(w_dic)
#下为解密：
n = input("请按规则输入页，行，列：")
temp_flag = True
for word in w_dic.keys():
    if n in w_dic[word]:
        print(word)
        flag = False
if not temp_flag:
    print("未输入正确格式。")

