import numpy as np
import matplotlib.pyplot as plt
import os # Importamos os para verificar si el archivo existe

# Define la ruta del archivo CSV
# Asegúrate de que 'citrus.csv' esté en el mismo directorio que tu script
# o especifica la ruta completa al archivo.
file_path = 'citrus.csv'

# --- Cargar los datos ---
# Usamos np.genfromtxt porque es robusto y puede manejar el encabezado.
# delimiter=',' indica que las columnas están separadas por comas.
# skip_header=1 indica que se omita la primera fila (el encabezado).
# usecols=(1, 2) indica que solo carguemos las columnas con índice 1 (diámetro)
# y 2 (peso). Recuerda que Python usa indexación base 0.
# Las columnas en el CSV son: nombre (0), diametro (1), peso (2), ...

# Verificamos si el archivo existe antes de intentar cargarlo
if not os.path.exists(file_path):
    print(f"Error: El archivo '{file_path}' no se encontró.")
    print("Asegúrate de que 'citrus.csv' está en el mismo directorio que este script.")
    # Puedes salir del script si el archivo no existe
    exit()

try:
    dato = np.genfromtxt(file_path, delimiter=',', skip_header=1, usecols=(1, 2))
    print("Datos cargados correctamente.")
    print(f"Forma de los datos cargados: {dato.shape}")
    # Verificamos si los datos tienen suficientes filas
    if dato.shape[0] < 10000:
        print("Advertencia: El archivo CSV parece tener menos de 10000 filas.")
        print("Asegúrate de que contiene al menos 5000 naranjas y 5000 toronjas según la descripción del ejercicio.")
except Exception as e:
    print(f"Ocurrió un error al cargar el archivo CSV: {e}")
    exit()


# --- Selección de datos (siguiendo las indicaciones del instructor) ---
# Las naranjas son las primeras 5000 filas.
# Las toronjas (grapefruit) comienzan en la fila 5000 hasta el final.
# La columna 0 en 'dato' es ahora el diámetro (era la columna 1 en el CSV original).
# La columna 1 en 'dato' es ahora el peso (era la columna 2 en el CSV original).

diametro_naranja = dato[:5000, 0]
diametro_toronja = dato[5000:, 0] # Desde la fila 5000 hasta el final
peso_naranja = dato[:5000, 1]
peso_toronja = dato[5000:, 1]   # Desde la fila 5000 hasta el final

print(f"Dimensiones del diámetro de naranja: {diametro_naranja.shape}")
print(f"Dimensiones del diámetro de toronja: {diametro_toronja.shape}")
print(f"Dimensiones del peso de naranja: {peso_naranja.shape}")
print(f"Dimensiones del peso de toronja: {peso_toronja.shape}")


# --- Visualización con Matplotlib ---
print("Creando el gráfico...")
# Crea una figura y ejes para el gráfico
plt.figure(figsize=(10, 6)) # Define el tamaño del gráfico (opcional)

# Grafica el peso en función del diámetro para naranjas
# Usamos '.' como marcador para mostrar puntos en lugar de una línea continua.
# alpha=0.5 hace que los puntos sean ligeramente transparentes (útil si hay muchos puntos superpuestos).
# label='Naranja' define la etiqueta para la leyenda.
plt.plot(diametro_naranja, peso_naranja, '.', label='Naranja', alpha=0.5, markersize=4)

# Grafica el peso en función del diámetro para toronjas
plt.plot(diametro_toronja, peso_toronja, '.', label='Toronja', alpha=0.5, markersize=4)

# Añade etiquetas a los ejes
plt.xlabel('Diámetro')
plt.ylabel('Peso')

# Añade un título al gráfico
plt.title('Peso vs. Diámetro para Naranjas y Toronjas')

# Muestra la leyenda para identificar qué puntos corresponden a cada fruta
plt.legend()

# Añade una cuadrícula al gráfico (opcional)
plt.grid(True)

# Muestra el gráfico
plt.show()

print("Script finalizado.")

'''
Por Gemini, citrus-4.png

Datos cargados correctamente.
Forma de los datos cargados: (10000, 2)
Dimensiones del diámetro de naranja: (5000,)
Dimensiones del diámetro de toronja: (5000,)
Dimensiones del peso de naranja: (5000,)
Dimensiones del peso de toronja: (5000,)
Creando el gráfico...
Script finalizado.
'''