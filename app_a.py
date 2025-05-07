import numpy as np
import matplotlib.pyplot as plt # Importamos la biblioteca para graficar

# --- Tu código existente ---
# Cargar datos desde el CSV ignorando la primera fila (encabezado)
# genfromtxt es útil porque maneja los valores 'nan' (Not a Number)
try:
    datos = np.genfromtxt("/home/pol/Descargas/manzanas.csv", delimiter=",", skip_header=1)

    print("Datos cargados correctamente. Forma:", np.shape(datos))
    # print("Contenido del archivo CSV:") # Evitamos imprimir todo si es muy grande
    # print(datos)

    # El array 'rango' no se usa para graficar los datos del CSV en este ejemplo,
    # pero lo mantenemos ya que estaba en tu código original.
    rango = np.arange(0, 10, 2)
    print("\nArreglo creado con np.arange(0, 10, 2):")
    print(rango)

    # --- Código para graficar ---

    print("\nGenerando gráfico...")

    # Creamos los valores para el eje X. Como cada fila de 'datos' tiene 90 columnas (basado en tu output),
    # podemos asumir que estas columnas representan puntos secuenciales (como el tiempo).
    # Creamos un array de 0 a 89 para el eje X.
    x_valores = np.arange(datos.shape[1])

    # Creamos la figura y los ejes del gráfico
    plt.figure(figsize=(10, 6)) # Define el tamaño de la figura (opcional)

    # Iteramos sobre cada fila de los datos para graficarla como una línea separada
    for i, fila_datos in enumerate(datos):
        # Graficamos la fila 'fila_datos' contra 'x_valores'
        # matplotlib maneja automáticamente los valores 'nan' (los puntos no se grafican)
        plt.plot(x_valores, fila_datos, label=f'Serie {i+1}') # Añadimos una etiqueta para la leyenda

    # Añadir títulos y etiquetas a los ejes
    plt.title('Gráfico de Series de Datos del CSV')
    plt.xlabel('Punto de Dato (Índice de Columna)')
    plt.ylabel('Valor')
    plt.grid(True) # Añadir una cuadrícula para mejor lectura
    plt.legend() # Mostrar la leyenda para identificar las series

    # Mostrar el gráfico
    plt.show()

except FileNotFoundError:
    print("Error: El archivo CSV no fue encontrado en la ruta especificada.")
except Exception as e:
    print(f"Ocurrió un error al cargar los datos o graficar: {e}")