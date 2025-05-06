import numpy as np

# Cargar los datos, ignorando la primera columna (nombres de ciudades)
datos = np.genfromtxt("/home/pol/Descargas/manzanas.csv", delimiter=",", skip_header=1, usecols=range(1, 88))

# Imprimir las dimensiones
print("Dimensiones de los datos:", datos.shape)

# Imprimir los datos de Moscú
print("Datos de Moscú:", datos[0])