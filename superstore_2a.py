import pandas as pd


datos_seleccion = pd.read_csv('superstore_data.csv', usecols = [0,1,4])
print(datos_seleccion.head())

'''
      Id  Year_Birth   Income
0   1826        1970  84835.0
1      1        1961  57091.0
2  10476        1958  67267.0
3   1386        1967  32474.0
4   5371        1989  21474.0
'''