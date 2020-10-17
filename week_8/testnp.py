import numpy as np

ls = [1,2,3]
ls1 = np.array([ls,[4,5,6]])
ls2 = np.array([[2,1,3],[1,4,6]])
ls3 = ls2 - ls1
print(ls3)
