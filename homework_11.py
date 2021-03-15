#將以下問卷資料的職業(Profession) 欄位缺失值填入字串 'others'，更進一步將字串做編碼。 此時用什麼方式做編碼比較適合？為什麼？



import pandas as pd 
q_df = pd.DataFrame([['male', 'teacher'], ['male', 'engineer'], ['female', None], ['female', 'engineer']],columns=['Sex','Profession'])
#print(q_df)
q_df['Profession'] = q_df['Profession'].fillna('others')
#print(q_df)
pf1 = pd.get_dummies(q_df[['Sex']])
print(pf1)
pf2 = pd.get_dummies(q_df[['Profession']])
print(pf2)
df = pd.concat([q_df, pf1,pf2], axis=1)
print(df)