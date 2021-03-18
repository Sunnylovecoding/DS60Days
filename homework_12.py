import pandas as pd
#題目 : 將資料夾中 boston.csv 讀進來，並用圖表分析欄位。
data = pd.read_csv('boston.csv')
#畫出箱型圖，並判斷哪個欄位的中位數在 300~400 之間？
print(type(data))
print(data.head())
data.boxplot()
#ANS:可知tax欄位的中位數落在300~400之間
#畫出散佈圖 x='NOX', y='DIS' ，並說明這兩欄位有什麼關係？
data.plot.scatter(x='NOX', y='DIS')
#ANS:NOX與DIS呈現負相關,隨NOX值增加,DIS值減少
