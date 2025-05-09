import numpy as np
import matplotlib.pyplot as plt

# Cargar datos ignorando la primera columna (que está llena de NaN)
data = np.genfromtxt('citrus.csv', delimiter=',', skip_header=1, usecols=range(1,6))

print("\nDatos válidos cargados:")
print("Forma del array:", data.shape)
print("Primeras filas:\n", data[:5])

# Dividir los datos (columnas 0 = diámetro, 1 = peso)
n_oranges = 5000
diam_naranja = data[:n_oranges, 0]  # Columna 0 (antes 1)
peso_naranja = data[:n_oranges, 1]   # Columna 1 (antes 2)
diam_toronja = data[n_oranges:, 0]
peso_toronja = data[n_oranges:, 1]

# Crear gráfico
plt.figure(figsize=(10,6))
plt.scatter(diam_naranja, peso_naranja, color='orange', alpha=0.7, label='Naranjas')
plt.scatter(diam_toronja, peso_toronja, color='red', alpha=0.7, label='Toronjas')
plt.title('Relación Diámetro-Peso')
plt.xlabel('Diámetro (cm)')
plt.ylabel('Peso (g)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

'''

Datos válidos cargados:
Forma del array: (10000, 5)
Primeras filas:
 [[  2.96  86.76 172.    85.     2.  ]
 [  3.91  88.05 166.    78.     3.  ]
 [  4.42  95.17 156.    81.     2.  ]
 [  4.47  95.6  163.    81.     4.  ]
 [  4.48  95.76 161.    72.     9.  ]]
                                        
'''