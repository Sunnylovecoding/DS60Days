"""

呈上題，將array中體重(weight)數據集取出算出全部平均體重
呈上題，進一步算出男生(sex欄位是boy)平均體重、女生(sex欄位是girl)平均體重
"""
import numpy as np
from numpy.core.defchararray import array
name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]

#將上列list依照['name','sex', 'weight', 'rank', 'myopia']順序擺入array，並且資料型態順序擺入[Unicode,Unicode,float,int,boolean]
dt = {'names':('name','sex', 'weight', 'rank', 'myopia'), 'formats':('U5','U5','f8','i8','?')}
c = np.zeros(8, dtype = dt)
c['name'] = name_list
c['sex'] = sex_list
c['weight'] = weight_list
c['rank'] = rank_list
c['myopia'] = myopia_list

#呈上題，將array中體重(weight)數據集取出算出全部平均體重
print(np.mean(c['weight']))
#呈上題，進一步算出男生(sex欄位是boy)平均體重、女生(sex欄位是girl)平均體重
boy_m = np.where(c['sex']=='boy')
boy_ans = np.mean(c['weight'][boy_m])
print(boy_ans)

girl_m = np.where(c['sex']=='girl')
girl_ans = np.mean(c['weight'][girl_m])
print(girl_ans)
