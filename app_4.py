import numpy as np

# Cargar los datos, ignorando la primera columna (nombres de ciudades)
datos = np.genfromtxt("/home/pol/Descargas/manzanas.csv", delimiter=",", skip_header=1, usecols=range(1, 88))

# Imprimir las dimensiones
print("Dimensiones de los datos:", datos.shape)

# Imprimir los datos de Moscú
print("Datos de Moscú:", datos[0])

'''
Dimensiones de los datos: (5, 87)
Datos de Moscú: [ 79.72  81.08  79.68  79.8   80.63  80.8   80.28  78.99  76.77  76.09
  76.36  77.16  77.5   79.03  80.28  80.05  78.11  76.9   77.68  76.05
  75.53  73.39  78.36  89.16 105.43 104.82 101.15  98.63  99.96  97.29
  98.64 104.26 102.63  98.64  97.17  98.09 103.07 110.26 110.84 112.28
 111.1  110.06 113.7  112.88 102.08  95.54  91.33  89.99  91.44  93.51
  93.6   93.78  98.91 121.76 129.6  127.9  114.55 101.88  99.09 103.35
 106.58 108.   114.95 121.17 122.48 127.58 131.89 129.36 104.26  93.45
  92.93  96.15  99.1  103.   103.31 103.01 107.37 116.91 125.29 123.94
 113.03 102.19  97.83 101.07 103.44 108.23 110.28]
'''