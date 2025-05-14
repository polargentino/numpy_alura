import pandas as pd

archivo = 'emisiones_CO2.xlsx'
intervalo = pd.read_excel(archivo, sheet_name='emisiones_C02', usecols='A:D', nrows=10)
print(intervalo)

print(pd.ExcelFile(archivo).sheet_names) # Para ver las hojas de Excel

'''
         País ISO 3166-1 alpha-3   Año  Total
0  Afganistán                AFG  1750      0
1  Afganistán                AFG  1751      0
2  Afganistán                AFG  1752      0
3  Afganistán                AFG  1753      0
4  Afganistán                AFG  1754      0
5  Afganistán                AFG  1755      0
6  Afganistán                AFG  1756      0
7  Afganistán                AFG  1757      0
8  Afganistán                AFG  1758      0
9  Afganistán                AFG  1759      0
['emisiones_C02', 'emisiones_percapita', 'fuentes']
                                                       
'''