import numpy as np
import cv2

img1 = cv2.imread("1.jpg")
int_img1 = img1.astype(np.int16)
img2 = cv2.imread(r"E:\Study\Grade2.one\Big_Data\week_8\2.jpg")
int_img2 = img2.astype(np.int16)
#cv2.imshow('src',img2)
#cv2.waitKey(0)
#print(img1.shape) # (h,w,c)
long = img1.shape[0]        #长度
width = img1.shape[1]       #宽度
pool = []       #存放对比后的图像。
diff_arr = int_img1 - int_img2
diff_arr = abs(diff_arr)


for i in range(10):
    for j in range(10):
        diff_sum = diff_arr[i*(long//10):(i+1)*(long//10),j*width//10:(j+1)*(width//10)].sum()
        if diff_sum > 100000:
            pool.append([])
            pool[i*10+j].append(img1[i*(long//10):(i+1)*long//10,j*(width//10):(j+1)*(width//10)])
            pool[i*10+j].append(img2[i*(long//10):(i+1)*long//10,j*(width//10):(j+1)*(width//10)])
        else:
            pool.append([])
            pool[i*10+j].append(img1[i*(long//10):(i+1)*(long//10),j*(width//10):(j+1)*(width//10)])


'''for i in range(len(pool)):
    print(len(pool[i]))

'''
out_img1 = np.zeros((long,width,3))
out_img2 = np.zeros((long,width,3))
for i in range(100):
    out_img1[i//10*long//10:(i//10+1)*long//10,i%10*width//10:(i%10+1)*width//10]= out_img1[i//10*long//10:(i//10+1)*long//10,i%10*width//10:(i%10+1)*width//10] + pool[i][0]

for i in range(100):
    out_img2[i//10*long//10:(i//10+1)*long//10,i%10*width//10:(i%10+1)*width//10]= out_img2[i//10*long//10:(i//10+1)*long//10,i%10*width//10:(i%10+1)*width//10] + pool[i][-1]

#out_img2 = out_img2.astype(np.uint8)     #还要把图片格式转回去，不然显示不出来。
#cv2.imshow('src',out_img2)
cv2.imshow('src',img2)
cv2.waitKey(0)

'''
1. 忘记老师上课讲的那个转化数字类型的方法了，，只好重新去网上找，但这个方法挺浪费空间的。
2. 感觉这个功能及其基类。。。就这个程序来说时毫无作用的。。。'''