import pandas as pd
#題目 : 將資料夾中 boston.csv 讀進來，並用圖表分析欄位。
data = pd.read_csv('boston.csv')
#畫出箱型圖，並判斷哪個欄位的中位數在 300~400 之間？
print(type(data))
print(data.head())

data.boxplot()
#畫出散佈圖 x='NOX', y='DIS' ，並說明這兩欄位有什麼關係？