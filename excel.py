import pandas as pd

archivo = 'emisiones_CO2.xlsx'
datos_co2 = pd.read_excel(archivo)
print(datos_co2)

'''
             País ISO 3166-1 alpha-3   Año         Total  ...       Cemento        Quema        Otros  Per Capita
0      Afganistán                AFG  1750  0.000000e+00  ...           NaN          NaN          NaN         NaN
1      Afganistán                AFG  1751  0.000000e+00  ...           NaN          NaN          NaN         NaN
2      Afganistán                AFG  1752  0.000000e+00  ...           NaN          NaN          NaN         NaN
3      Afganistán                AFG  1753  0.000000e+00  ...           NaN          NaN          NaN         NaN
4      Afganistán                AFG  1754  0.000000e+00  ...           NaN          NaN          NaN         NaN
...           ...                ...   ...           ...  ...           ...          ...          ...         ...
63099      Global                WLD  2017  3.609674e+10  ...  1.507923e+09  391992176.0  302294047.0   4749682.0
63100      Global                WLD  2018  3.682651e+10  ...  1.569218e+09  412115746.0  302478706.0   4792753.0
63101      Global                WLD  2019  3.708256e+10  ...  1.617507e+09  439253991.0  306638573.0   4775633.0
63102      Global                WLD  2020  3.526409e+10  ...  1.637538e+09  407583673.0  296301685.0   4497423.0
63103      Global                WLD  2021  3.712385e+10  ...  1.672592e+09  416525563.0  296145746.0   4693699.0

[63104 rows x 11 columns]
'''
print(pd.ExcelFile(archivo).sheet_names) # Para ver las hojas de Excel

'''
['emisiones_C02', 'emisiones_percapita', 'fuentes']
'''