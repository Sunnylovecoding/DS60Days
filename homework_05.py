"""
題目：

上 3 列共六位同學的英文、數學、國文成績，第一個元素代表第一位同學，舉例第一位同學英文 55 分、數學 60 分、國文 65 分，今天第五位同學因某原因沒來考試，導致數學成績缺值，運用上列數據回答下列問題。

請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略？
第五位同學補考數學後成績為 55，請計算補考後數學成績平均、最大值、最小值、標準差？
用補考後資料找出與國文成績相關係數最高的學科？
"""
import numpy as np

english_score = np.array([55,89,76,65,48,70])

math_score = np.array([60,85,60,68,np.nan,60])

chinese_score = np.array([65,90,82,72,66,77])

#請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略？
#英文

mean_eng = np.mean(english_score)
print('英文平均:',mean_eng)
max_eng = np.amax(english_score)
print('英文最大值:',max_eng)
min_eng = np.amin(english_score)
print('英文最小值:',min_eng)
std_eng = np.std(english_score)
print('英文標準差:',std_eng)
#國文
mean_ch = np.mean(chinese_score)
print('國文平均:',mean_ch)
max_ch = np.amax(chinese_score)
print('國文最大值:',max_ch)
min_ch = np.amin(chinese_score)
print('國文最小值:',min_ch)
std_ch = np.std(chinese_score)
print('國文標準差:',std_ch)
#數學
mean_math = np.nanmean(math_score)
print('數學平均:',mean_math)
max_math = np.nanmax(math_score)
print('數學最大值:',max_math)
min_math = np.nanmin(math_score)
print('數學最小值:',min_math)
std_math = np.nanstd(math_score)
print('數學標準差:',std_math)


#第五位同學補考數學後成績為 55，請計算補考後數學成績平均、最大值、最小值、標準差？
math_fixscore = np.array([60,85,60,68,55,60])
mean_mathf = np.mean(math_fixscore)
print('數學補考平均:',mean_mathf)
max_mathf = np.amax(math_fixscore)
print('數學補考最大值:',max_mathf)
min_mathf = np.amin(math_fixscore)
print('數學補考最小值:',min_mathf)
std_mathf = np.std(math_fixscore)
print('數學補考標準差:',std_mathf)
#用補考後資料找出與國文成績相關係數最高的學科？
group = np.concatenate((english_score,math_fixscore,chinese_score)).reshape(3,6)
ans = np.corrcoef(group)
print(ans)