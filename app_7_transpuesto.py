import pandas as pd

# Cargar el CSV con pandas
df = pd.read_csv("/home/pol/Descargas/manzanas.csv")

# Imprimir las dimensiones originales
print("Dimensiones de los datos originales:", df.shape)

# Transponer el DataFrame
df_transpuesto = df.T

# Imprimir las dimensiones del DataFrame transpuesto
print("Dimensiones de los datos transpuestos:", df_transpuesto.shape)

# Imprimir los datos transpuestos (primeras filas)
print("Datos transpuestos (primeras filas):")
print(df_transpuesto.head())

'''
Dimensiones de los datos originales: (5, 88)
Dimensiones de los datos transpuestos: (88, 5)
Datos transpuestos (primeras filas):
                0             1            2          3              4
Unnamed: 0  Moscu  Kaliningrado  Petersburgo  Krasnodar  Ekaterimburgo
1.2013      79.72         42.67        62.55      48.26          71.25
2.2013      81.08         44.37        62.73      51.01          71.35
3.2013      79.68         44.73        63.43      50.91           70.9
4.2013       79.8         46.75        63.83      53.94          71.92
'''