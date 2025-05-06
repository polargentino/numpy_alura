import pandas as pd

# Cargar el CSV con pandas
df = pd.read_csv("/home/pol/Descargas/manzanas.csv")

# Imprimir las dimensiones
print("Dimensiones de los datos:", df.shape)

# Imprimir los datos de Moscú como lista de floats
print("Datos de Moscú:", [float(x) for x in df.iloc[0, 1:].values])