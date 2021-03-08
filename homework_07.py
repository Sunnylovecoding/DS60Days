import numpy as np
#運用上列array計算反矩陣，乘上原矩陣，並觀察是否為單位矩陣?

array1 = np.array([[10, 8], [3, 5]])
#反矩陣
array_inv = np.linalg.inv(array1)
print(array_inv)
#乘上原矩陣
ans = array1 @ array_inv
print(ans) #是為單位矩陣

#運用上列array計算特徵值、特徵向量?
w,v = np.linalg.eig(array1)
print(w)
print(v)
#運用上列array計算SVD?
print('----------------------------------')
u,s,vh = np.linalg.svd(array1)
print(u)
print(s)
print(vh)