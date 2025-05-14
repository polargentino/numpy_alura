import pandas as pd

archivo = 'emisiones_CO2.xlsx'
percapita = pd.read_excel(archivo, sheet_name='emisiones_percapita') # ['emisiones_C02', 'emisiones_percapita', 'fuentes']
print(percapita.sample(5)) # 5 registros aleatorios

'''
             País ISO 3166-1 alpha-3   Año      Total     Carbón    Aceite  Gas  Cemento  Quema  Otros
878       Andorra                AND  1812        NaN        NaN       NaN  NaN      NaN    NaN    NaN
35149   Martinica                MTQ  1811        NaN        NaN       NaN  NaN      NaN    NaN    NaN
40307     Nigeria                NGA  1801        NaN        NaN       NaN  NaN      NaN    NaN    NaN
26314     Irlanda                IRL  1952  3283901.0  2834261.0  371481.0  0.0  78160.0    0.0    NaN
36876  Montenegro                MNE  1906        NaN        NaN       NaN  NaN      NaN    NaN    NaN
'''