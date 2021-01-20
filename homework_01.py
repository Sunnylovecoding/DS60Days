import numpy as np
#建立數列
a = np.arange(0, 21, 1)
print(a)
#取出偶數值
mask1 = a[::2]
print (mask1)
#取出符合3倍數的數值
mask2 = a[3::3]
print(mask2) 