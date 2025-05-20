import pandas as pd
df_data = pd.read_json('inmuebles_disponibles.json')
print(df_data.head())
'''
    id       fecha  lugar_disponible precio
0  857  2016-01-04             False   None
1  857  2016-01-05             False   None
2  857  2016-01-06             False   None
3  857  2016-01-07             False   None
4  857  2016-01-08             False   None
'''
print(df_data.info())
'''
<class 'pandas.core.frame.DataFrame'>
Index: 365000 entries, 0 to 364999
Data columns (total 4 columns):
 #   Column            Non-Null Count   Dtype 
---  ------            --------------   ----- 
 0   id                365000 non-null  int64 
 1   fecha             365000 non-null  object
 2   lugar_disponible  365000 non-null  bool  
 3   precio            270547 non-null  object
dtypes: bool(1), int64(1), object(2)
memory usage: 11.5+ MB
None
'''