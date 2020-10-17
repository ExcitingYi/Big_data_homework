import os
def judge(a):       #判断是否为字母，若为字母，小写输出。
    flag = True
    if a < "A" or "Z" < a < "a" or "z" < a:
        flag = False
    if flag:
        if "A" <= a <= "Z":
            a = chr(ord(a) + ord("a") - ord("A"))
        return a
    else:
        return flag

#批量读取文件，代码参考 https://blog.csdn.net/ayouleyang/article/details/102746267?biz_id=102&utm_term=python%E6%89%B9%E9%87%8F%E8%AF%BB%E5%8F%96txt%E6%96%87%E4%BB%B6&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-2-102746267&spm=1018.2118.3001.4187
w_dic = {}
for i in range(26):
    w_dic[chr(ord("a")+i)] = 0

path = "E:\Study\Grade2.one\Big_Data\week_4\VOA语料" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
txts = []
for file in files: #遍历文件夹
    position = path+'\\'+ file #构造绝对路径，"\\"，其中一个'\'为转义符
    #print (position)
    with open(position, "r",encoding='utf-8') as f:    #打开文件
        data = f.read()   #读取文件
        for word in data:
            if judge(word):
                txts.append(judge(word))
                w_dic[judge(word)] += 1

#词频统计：
w_ls = list(w_dic.items())
w_ls.sort(key=lambda x:x[1],reverse=True)
sorted_w_ls_1 = []
sorted_w_dic_1 = {}

for i in range(len(w_ls)):
    sorted_w_ls_1.append(w_ls[i][0])
    sorted_w_dic_1[i] = w_ls[i][0]


sec_w = input("plz enter the txt:")
sec_ls = []
#w_dic 上面用完就没用了，数据都已经放在sorted的字典和列表里了，所以这个列表现在重新用。
w_dic = {}
for i in range(26):
    w_dic[chr(ord("a")+i)] = 0
#词频统计
for i in sec_w:
    if judge(i):
        w_dic[judge(i)] += 1
#同样，上面用完就没啥用了。
w_ls = list(w_dic.items())
w_ls.sort(key=lambda x:x[1],reverse=True)
sorted_w_ls_2 = []
sorted_w_dic_2 = {}
for i in range(len(w_ls)):
    sorted_w_ls_2.append(w_ls[i][0])
    sorted_w_dic_2[w_ls[i][0]] = i
    #这个dic_2和上面dic_1不一样，1 是key:数字，value:字母，这个是key：字母，value:数字，方便直接检索。

out_ls = []
for i in sec_w:
    if judge(i):
        out_ls.append(sorted_w_dic_1[sorted_w_dic_2[judge(i)]])
    else:
        out_ls.append(i)
#print(sorted_w_ls_1)




"以上为破译，下为检验。"



path = "E:\Study\Grade2.one\Big_Data\week_4\VOA语料" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称

words_pool = []
for file in files: #遍历文件夹
    position = path+'\\'+ file #构造绝对路径，"\\"，其中一个'\'为转义符
    #print (position)
    with open(position, "r",encoding='utf-8') as f:    #打开文件
        for i in f.readlines():
            words_pool.extend(i.split(" "))

for i in range(len(words_pool)):
    words_pool[i] = words_pool[i].replace("\n","")
    temp = words_pool[i]
    words_pool[i] = ""
    for j in temp:
        if judge(j):
            words_pool[i] += judge(j)

new = "".join(out_ls)
new_out_ls = new.split(" ") #原本为一个单词一个元素，现是一个词一个元素。

judge_sum = 0
for i in new_out_ls:
    if i in words_pool:
        judge_sum+=1


if judge_sum / len(out_ls) > 0.7:       #若百分之七十的单词在原有的词库里，则算破译成功。
    print("破译成功！")
    print("".join(out_ls))
else:
    print("破译失败。结果为：")
    print("".join(out_ls))


