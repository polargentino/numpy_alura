import pandas as pd

archivo = 'emisiones_CO2.xlsx'
fuentes = pd.read_excel(archivo, sheet_name='fuentes') # ['emisiones_C02', 'emisiones_percapita', 'fuentes']
print(fuentes.tail()) # 5 últimos registros

'''
         País ISO 3166-1 alpha-3   Año  ...               Quema   Otros                                         Per Capita
63099  Global                WLD  2017  ...  CDIAC 2022 and GCP  [NONE]  CDIAC 2022, BP, Sum of countries, and UN popul...
63100  Global                WLD  2018  ...  CDIAC 2022 and GCP  [NONE]  CDIAC 2022, BP, Sum of countries, and UN popul...
63101  Global                WLD  2019  ...  CDIAC 2022 and GCP  [NONE]  CDIAC 2022, BP, Sum of countries, and UN popul...
63102  Global                WLD  2020  ...  CDIAC 2022 and GCP  [NONE]  CDIAC 2022, BP, Sum of countries, and UN popul...
63103  Global                WLD  2021  ...  CDIAC 2022 and GCP  [NONE]  CDIAC 2022, BP, Sum of countries, and UN popul...

[5 rows x 11 columns]
                       
'''