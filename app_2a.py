import numpy as np

# URL CORRECTA del archivo CSV
url = 'https://gist.githubusercontent.com/ahcamachod/9be09de793dc3bf1e6c3d98eb4e5b1ef/raw/21b85572693200040e11284ef6dcfc3457ec8e11/citrus.csv'

try:
    # Cargar datos desde la URL
    # delimiter=',' especifica que los valores están separados por comas
    # usecols=np.arange(1, 6, 1) selecciona las columnas con índices 1, 2, 3, 4, 5
    # skiprows=1 omite la primera fila (encabezado)
    datos = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 6, 1), skiprows=1)

    # Imprimir la forma original del array cargado
    print("La forma original de los datos cargados es:")
    print(np.shape(datos)) # Debería ser (10000, 5)

    # ====== Incorporar Transposición ======
    # Aplicar la transposición (.T) al array datos
    datos_transpuestos = datos.T
    # ======================================

    # Imprimir la forma del array transpuesto
    print("\nLa forma de los datos transpuestos es:")
    print(np.shape(datos_transpuestos)) # Debería ser (5, 10000)

    # Opcional: Imprimir los primeros elementos del array transpuesto para verificar
    # print("\nLos primeros elementos de los datos transpuestos son:")
    # print(datos_transpuestos[:, :5]) # Muestra las 5 filas (originalmente columnas) y las primeras 5 columnas (originalmente filas)

except Exception as e:
    # Captura errores potenciales como problemas de red o URL inválida
    print(f"Ocurrió un error al cargar los datos: {e}")
    print("Verifica la URL y tu conexión a internet.")

'''
La forma original de los datos cargados es:
(10000, 5)

La forma de los datos transpuestos es:
(5, 10000)
            
'''