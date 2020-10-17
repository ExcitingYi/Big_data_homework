import numpy as np
import cv2

img1 = cv2.imread("1.jpg")
img1 = img1.astype(np.int16)
img2 = cv2.imread("2.jpg")
img2 = img2.astype(np.int16)
#cv2.imshow('src',img)
print(img1.shape) # (h,w,c)
long = img1.shape[0]
width = img1.shape[1]
pool = []       #存放对比后的图像。
diff_arr = img1 - img2
diff_arr = abs(diff_arr)

for i in range(10):
    for j in range(10):
        temp_arr = diff_arr[i*long//10:(i+1)*long//10-1][j*width//10:(i+1)*width//10-1]
        if temp_arr.sum() > 100000:
            pool.append([])
            pool[i*10+j].append(list(img1[i*long//10:(i+1)*long//10-1][j*width//10:(i+1)*width//10-1].tolist()))
            pool[i*10+j].append(list(img2[i*long//10:(i+1)*long//10-1][j*width//10:(i+1)*width//10-1].tolist()))
        else:
            pool.append([])
            pool[i*10+j].append(list(img1[i*long//10:(i+1)*long//10-1][j*width//10:(i+1)*width//10-1].tolist()))


print(len(pool[1][0][0]))
print(np.array(pool[1]).shape)
out_img = np.zeros((long,width,3))
k1 = 0
k2 = 0
for i in range(100):
    out_img[i//10*long//10:(i//10+1)*long//10-1][i%10*width//10:(i%10+1)*width//10-1] = out_img[i//10*long//10:(i//10+1)*long//10-1][i%10*width//10:(i%10+1)*width//10-1] + np.array(pool[i][0])




