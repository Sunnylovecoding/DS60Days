#讀取資料夾中boston.csv讀取其欄位CHAS、NOX、RM，輸出成.xlsx檔案
import pandas as pd
boston_data = pd.read_csv('boston.csv',usecols = ['CHAS','NOX','RM'])
print(boston_data)
boston_data.to_excel('myboston.xlsx', sheet_name='boston_data')
