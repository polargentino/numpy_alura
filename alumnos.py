# Importamos la biblioteca Pandas, que nos permite trabajar con datos en forma de DataFrames
import pandas as pd

# URL del archivo CSV que vamos a importar
url = 'https://gist.githubusercontent.com/ahcamachod/807a2c1cf6c19108b2b701ea1791ab45/raw/fb84f8b2d8917a89de26679eccdbc8f9c1d2e933/alumnos.csv'

# Leemos el archivo CSV desde la URL y lo almacenamos en un DataFrame de Pandas
datos = pd.read_csv(url)

# Visualizamos las primeras 7 filas del DataFrame
primeras_filas = datos.head(7)
print("Primeras 7 filas del DataFrame:\n", primeras_filas)

# Visualizamos las últimas 5 filas del DataFrame
ultimas_filas = datos.tail(5)
print("\nÚltimas 5 filas del DataFrame:\n", ultimas_filas)

# Obtenemos la cantidad de filas y columnas en el DataFrame
filas, columnas = datos.shape
print(f"\nEl DataFrame tiene {filas} filas y {columnas} columnas.")

# Exploramos los nombres de las columnas del DataFrame
columnas = datos.columns
print("\nColumnas del DataFrame:\n", columnas)

# Analizamos los tipos de datos presentes en cada columna
tipos_de_datos = datos.dtypes
print("\nTipos de datos en cada columna:\n", tipos_de_datos)

# Calculamos algunas estadísticas descriptivas básicas de los datos en el DataFrame
estadisticas = datos.describe()
print("\nEstadísticas descriptivas:\n", estadisticas)

'''
Primeras 7 filas del DataFrame:
     Nombre  Edad  Nota Aprobado
0  Alberto    20   7.5     True
1      Ana    18   NaN    False
2   Camila    27   2.5    False
3    David    18   5.0    False
4    Brian    21  10.0     True
5    Bruna    23   NaN    False
6  Daniela    21   7.0     True

Últimas 5 filas del DataFrame:
     Nombre  Edad  Nota   Aprobado
13  Miriam    25   9.0       True
14   Pablo    37   NaN      False
15  Milena    29   7.0       True
16   Lucas    33   NaN      False
17   Nadia    34   8.0  Verdadero

El DataFrame tiene 18 filas y 4 columnas.

Columnas del DataFrame:
 Index(['Nombre', 'Edad', 'Nota', 'Aprobado'], dtype='object')

Tipos de datos en cada columna:
 Nombre       object
Edad          int64
Nota        float64
Aprobado     object
dtype: object

Estadísticas descriptivas:
             Edad       Nota
count  18.000000  12.000000
mean   25.500000   6.841667
std     6.070662   2.264532
min    18.000000   2.500000
25%    21.000000   5.450000
50%    24.500000   7.000000
75%    28.750000   8.250000
max    37.000000  10.000000
                            

Explicación de Mistral AI:
-------------------------

Explicación del código:
Importación de Pandas: Importamos la biblioteca Pandas, que es esencial para el manejo y análisis de 
datos en Python.

URL del archivo CSV: Definimos la URL del archivo CSV que queremos importar.

Lectura del archivo CSV: Utilizamos pd.read_csv() para leer el archivo CSV desde la URL y almacenarlo 
en un DataFrame llamado datos.

Visualización de las primeras y últimas filas: Usamos head(7) para ver las primeras 7 filas y tail(5) 
para ver las últimas 5 filas del DataFrame.

Cantidad de filas y columnas: Utilizamos el atributo shape para obtener la cantidad de filas y 
columnas en el DataFrame.

Exploración de columnas y tipos de datos: Usamos columns para ver los nombres de las columnas y 
dtypes para ver los tipos de datos en cada columna.

Estadísticas descriptivas: Utilizamos el método describe() para calcular estadísticas descriptivas 
básicas de los datos en el DataFrame.


Primeras 7 filas del DataFrame:

Muestra las primeras 7 filas del DataFrame, incluyendo los nombres, edades, notas y si los alumnos 
han aprobado.

Observa que hay valores NaN en la columna "Nota", lo que indica datos faltantes.
Últimas 5 filas del DataFrame:

Muestra las últimas 5 filas del DataFrame.
Nuevamente, hay valores NaN en la columna "Nota" y un valor "Verdadero" en lugar de True en la columna "Aprobado" para Nadia, lo cual podría ser un error de consistencia en los datos.
Cantidad de filas y columnas:

El DataFrame tiene 18 filas y 4 columnas.
Columnas del DataFrame:

Las columnas son: "Nombre", "Edad", "Nota" y "Aprobado".
Tipos de datos en cada columna:

"Nombre" y "Aprobado" son de tipo object (generalmente cadenas de texto o valores mixtos).
"Edad" es de tipo int64 (números enteros).
"Nota" es de tipo float64 (números decimales).
Estadísticas descriptivas:

Proporciona un resumen estadístico de las columnas numéricas ("Edad" y "Nota").
Para "Edad":
count: 18 valores no nulos.
mean: La edad promedio es 25.5.
std: La desviación estándar es aproximadamente 6.07.
min: La edad mínima es 18.
25%, 50%, 75%: Los percentiles 25, 50 (mediana) y 75.
max: La edad máxima es 37.
Para "Nota":
count: 12 valores no nulos (hay 6 valores faltantes).
mean: La nota promedio es aproximadamente 6.84.
std: La desviación estándar es aproximadamente 2.26.
min: La nota mínima es 2.5.
25%, 50%, 75%: Los percentiles 25, 50 (mediana) y 75.
max: La nota máxima es 10.0.



'''
