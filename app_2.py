import numpy as np

# URL CORRECTA del archivo CSV
url = 'https://gist.githubusercontent.com/ahcamachod/9be09de793dc3bf1e6c3d98eb4e5b1ef/raw/21b85572693200040e11284ef6dcfc3457ec8e11/citrus.csv'

try:
    # Cargar datos desde la URL
    # delimiter=',' especifica que los valores están separados por comas
    # usecols=np.arange(1, 6, 1) selecciona las columnas con índices 1, 2, 3, 4, 5
    # skiprows=1 omite la primera fila (encabezado)
    datos = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 6, 1), skiprows=1)

    # Imprimir la forma del array cargado (filas, columnas)
    print("La forma de los datos cargados es:")
    print(np.shape(datos))

    # Opcional: Imprimir los primeros elementos para verificar
    # print("\nLos primeros 5 elementos de los datos son:")
    # print(datos[:5])

except Exception as e:
    # Captura errores potenciales como problemas de red o URL inválida
    print(f"Ocurrió un error al cargar los datos: {e}")
    print("Verifica la URL y tu conexión a internet.")

'''
La forma de los datos cargados es:
(10000, 5)


https://gist.githubusercontent.com/ahcamachod/9be09de793dc3bf1e6c3d98eb4e5b1ef/raw/21b85572693200040e11284ef6dcfc3457ec8e11/citrus.csv:

nombre,diametro,peso,rojo,verde,azul
naranja,2.96,86.76,172,85,2
naranja,3.91,88.05,166,78,3
naranja,4.42,95.17,156,81,2
naranja,4.47,95.6,163,81,4
naranja,4.48,95.76,161,72,9
naranja,4.59,95.86,142,100,2
naranja,4.64,97.94,156,85,2
naranja,4.65,98.5,142,74,2
naranja,4.68,100.2,159,90,16
naranja,4.69,100.31,161,76,6
naranja,4.73,101.33,148,88,2

Explicación:
-----------

La salida (10000, 5) tiene una relación directa con la estructura del archivo .csv que mostraste y 
los parámetros que usaste en np.loadtxt.

Veamos la relación:

Tu archivo .csv tiene la siguiente estructura (encabezado):

nombre,diametro,peso,rojo,verde,azul
Esto son 6 columnas en total.

En tu código usaste np.loadtxt con estos parámetros clave:

skiprows=1: Le dijiste a NumPy que omitiera la primera fila del archivo. Esa primera fila es el 
encabezado (nombre,diametro,peso,rojo,verde,azul).

usecols=np.arange(1, 6, 1): Esto le dice a NumPy que solo cargue ciertas columnas. np.arange(1, 6, 1) 
crea una secuencia de números [1, 2, 3, 4, 5]. En programación, los índices de columna a menudo 
empiezan desde 0. Así que esto significa que cargaste las columnas con índice:

1 (que corresponde a diametro)
2 (que corresponde a peso)
3 (que corresponde a rojo)
4 (que corresponde a verde)
5 (que corresponde a azul)

La columna 0 (nombre) fue omitida intencionalmente (o por defecto, ya que loadtxt con dtype=float 
espera números y la columna nombre contiene texto).

Relación con la salida (10000, 5):

El número 5 en (10000, 5) representa la cantidad de columnas que cargaste. Cargaste exactamente 5 
columnas (diametro, peso, rojo, verde, azul) usando usecols.

El número 10000 en (10000, 5) representa la cantidad de filas de datos que se cargaron. Después de 
omitir la primera fila (el encabezado), el archivo .csv tiene 10000 filas con los datos de las frutas.

En resumen, (10000, 5) te dice que cargaste correctamente 10000 registros (filas) y cada registro 
contiene 5 valores numéricos (las columnas diametro, peso, rojo, verde, azul) de tu archivo CSV.
'''