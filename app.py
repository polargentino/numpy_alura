

import numpy as np

# Cargar datos desde el CSV ignorando la primera fila (encabezado)
datos = np.genfromtxt("/home/pol/Descargas/manzanas.csv", delimiter=",", skip_header=1)

# Mostrar el contenido
print("Contenido del archivo CSV:")
print(datos)

# Crear un arreglo con np.arange
rango = np.arange(0, 10, 2)
print("\nArreglo creado con np.arange(0, 10, 2):")
print(rango)

