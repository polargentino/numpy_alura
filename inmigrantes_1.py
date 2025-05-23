import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('inmigrantes_canada.csv')
print(df.head())

print(df.shape)
print(df.info())

df.set_index('Pais',inplace=True)
print(df)

años = list(map(str,range(1980,2014)))
print(años)

colombia = df.loc['Colombia',años]
print(colombia)

col_dict = {'Año':colombia.index.tolist(),
            'Inmigrantes':colombia.values.tolist()}


sudamerica = df.query('Region == "América del Sur"')
print(sudamerica.head(10))

colores = ['royalblue','orange','forestgreen','orchid',
           'purple','brown','slateblue','gray','olive',
           'navy','teal','tomato']

fig, ax = plt.subplots(figsize=(10,3))

ax.bar(sudamerica.index, sudamerica['Total'], color=colores)
ax.set_title('Inmigración de sudamericanos hacia Canadá\ndurante el periodo de 1980 a 2013', fontsize=18, loc='left')
ax.set_xlabel('Paises')
ax.set_ylabel('Número de Inmigrantes', fontsize=14)

ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)
ax.grid(linestyle='--')
plt.show()

'''
              Pais Continente           Region  1980  1981  1982  ...  2009  2010  2011  2012  2013  Total
0       Afganistán       Asia      Sur de Asia    16    39    39  ...  1746  1758  2203  2635  2004  58639
1          Albania     Europa    Sur de Europa     1     0     0  ...   716   561   539   620   603  15699
2          Argelia     África  Norte de África    80    67    71  ...  5393  4752  4325  3774  4331  69439
3  Samoa Americana    Oceanía        Polinesia     0     1     0  ...     0     0     0     0     0      6
4          Andorra     Europa    Sur de Europa     0     0     0  ...     0     0     0     1     1     15

[5 rows x 38 columns]
(195, 38)
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 195 entries, 0 to 194
Data columns (total 38 columns):
 #   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   Pais        195 non-null    object
 1   Continente  195 non-null    object
 2   Region      195 non-null    object
 3   1980        195 non-null    int64 
 4   1981        195 non-null    int64 
 5   1982        195 non-null    int64 
 6   1983        195 non-null    int64 
 7   1984        195 non-null    int64 
 8   1985        195 non-null    int64 
 9   1986        195 non-null    int64 
 10  1987        195 non-null    int64 
 11  1988        195 non-null    int64 
 12  1989        195 non-null    int64 
 13  1990        195 non-null    int64 
 14  1991        195 non-null    int64 
 15  1992        195 non-null    int64 
 16  1993        195 non-null    int64 
 17  1994        195 non-null    int64 
 18  1995        195 non-null    int64 
 19  1996        195 non-null    int64 
 20  1997        195 non-null    int64 
 21  1998        195 non-null    int64 
 22  1999        195 non-null    int64 
 23  2000        195 non-null    int64 
 24  2001        195 non-null    int64 
 25  2002        195 non-null    int64 
 26  2003        195 non-null    int64 
 27  2004        195 non-null    int64 
 28  2005        195 non-null    int64 
 29  2006        195 non-null    int64 
 30  2007        195 non-null    int64 
 31  2008        195 non-null    int64 
 32  2009        195 non-null    int64 
 33  2010        195 non-null    int64 
 34  2011        195 non-null    int64 
 35  2012        195 non-null    int64 
 36  2013        195 non-null    int64 
 37  Total       195 non-null    int64 
dtypes: int64(35), object(3)
memory usage: 58.0+ KB
None
                  Continente            Region  1980  1981  1982  1983  ...  2009  2010  2011  2012  2013  Total
Pais                                                                    ...                                     
Afganistán              Asia       Sur de Asia    16    39    39    47  ...  1746  1758  2203  2635  2004  58639
Albania               Europa     Sur de Europa     1     0     0     0  ...   716   561   539   620   603  15699
Argelia               África   Norte de África    80    67    71    69  ...  5393  4752  4325  3774  4331  69439
Samoa Americana      Oceanía         Polinesia     0     1     0     0  ...     0     0     0     0     0      6
Andorra               Europa     Sur de Europa     0     0     0     0  ...     0     0     0     1     1     15
...                      ...               ...   ...   ...   ...   ...  ...   ...   ...   ...   ...   ...    ...
Vietnam                 Asia  Sudeste Asiático  1191  1829  2162  3404  ...  2171  1942  1723  1731  2112  97146
Sahara Occidental     África   Norte de África     0     0     0     0  ...     0     0     0     0     0      2
Yemen                   Asia   Asia Occidental     1     2     1     6  ...   128   211   160   174   217   2985
Zambia                África   África Oriental    11    17    11     7  ...    60   102    69    46    59   1677
Zimbabue              África   África Oriental    72   114   102    44  ...   508   494   434   437   407   8598

[195 rows x 37 columns]
['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013']
1980     266
1981     326
1982     360
1983     244
1984     235
1985     214
1986     257
1987     376
1988     352
1989     439
1990     614
1991     652
1992     582
1993     464
1994     375
1995     371
1996     381
1997     578
1998     929
1999    1306
2000    2259
2001    2965
2002    3283
2003    4318
2004    4566
2005    6424
2006    6535
2007    5357
2008    5452
2009    4652
2010    5218
2011    4366
2012    3741
2013    3631
Name: Colombia, dtype: object
                           Continente           Region  1980  1981  1982  ...  2010  2011  2012  2013  Total
Pais                                                                      ...                               
Argentina  América Latina y el Caribe  América del Sur   368   426   626  ...   459   278   263   282  19596
Bolivia    América Latina y el Caribe  América del Sur    44    52    42  ...   180    86    83   107   3205
Brasil     América Latina y el Caribe  América del Sur   211   220   192  ...  2598  1508  1642  1714  29659
Chile      América Latina y el Caribe  América del Sur  1233  1069  1078  ...   340   174   291   273  21359
Colombia   América Latina y el Caribe  América del Sur   266   326   360  ...  5218  4366  3741  3631  72088
Ecuador    América Latina y el Caribe  América del Sur   238   207   184  ...   353   348   282   418  12233
Guyana     América Latina y el Caribe  América del Sur  2334  2943  3575  ...   953   804   676   656  75785
Paraguay   América Latina y el Caribe  América del Sur    45    26    32  ...    89    83    55    66   1944
Perú       América Latina y el Caribe  América del Sur   317   456   401  ...  1283   886   787   682  32652
Surinam    América Latina y el Caribe  América del Sur    15    10    21  ...    13    11    16     4    739
'''