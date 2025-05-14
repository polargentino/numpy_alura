import pandas as pd


clientes_mercado = pd.read_csv('clientes_mercado.csv')
print(clientes_mercado)
'''
Sin especificar index=False: 

      Unnamed: 0     Id  Year_Birth   Income
0              0   1826        1970  84835.0
1              1      1        1961  57091.0
2              2  10476        1958  67267.0
3              3   1386        1967  32474.0
4              4   5371        1989  21474.0
...          ...    ...         ...      ...
2235        2235  10142        1976  66476.0
2236        2236   5263        1977  31056.0
2237        2237     22        1976  46310.0
2238        2238    528        1978  65819.0
2239        2239   4070        1969  94871.0

[2240 rows x 4 columns]


datos_seleccion.to_csv('clientes_mercado.csv', index=False)

         Id  Year_Birth   Income
0      1826        1970  84835.0
1         1        1961  57091.0
2     10476        1958  67267.0
3      1386        1967  32474.0
4      5371        1989  21474.0
...     ...         ...      ...
2235  10142        1976  66476.0
2236   5263        1977  31056.0
2237     22        1976  46310.0
2238    528        1978  65819.0
2239   4070        1969  94871.0

[2240 rows x 3 columns]
                        
'''