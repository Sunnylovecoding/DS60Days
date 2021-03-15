#讀取 STOCK_DAY_0050_202009.csv 串聯 STOCK_DAY_0050_202010.csv，並且找出 open 小於 close 的資料
import pandas as pd
stockdata_1 = pd.read_csv('STOCK_DAY_0050_202009.csv')
#print(stockdata_1)
stockdata_2 = pd.read_csv('STOCK_DAY_0050_202010.csv')
#print(stockdata_2)
stockdata_3 = pd.concat([stockdata_1,stockdata_2],axis=0, join='inner')
print(stockdata_3)
ans = stockdata_3[stockdata_3.open <stockdata_3.close]
print(ans)
print(ans.count())