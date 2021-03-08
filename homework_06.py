"""
多陣列存一起需要存成npz，讀取須注意npz中有多個陣列
題目:
#1.將下兩列array存成npz檔


"""
import numpy as np
array1 = np.array(range(30))
array2 = np.array([2,3,5])
#print(array1,array2)
np.savez('array.npz',array1=array1, array2=array2)

#2.讀取剛剛的npz檔，加入下列array一起存成新的npz檔
array3 = np.array([[4,5,6], [1,2,3]])
load_new = np.load ('array.npz')
np.savez('array2.npz',load_new['array1'] ,load_new['array2'],array3 )
print(np.load('array2.npz'))
