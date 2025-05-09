'''
Ahora que conocemos la estructura de los datos y hemos identificado las columnas con valores 
faltantes, el siguiente paso lógico en la exploración inicial es obtener estadísticas descriptivas 
de las columnas numéricas. Esto nos da una idea de la distribución de los valores (promedio, valores 
mínimos y máximos, etc.).

Podemos usar el método .describe() para esto.
'''
# Importamos la librería pandas (si no la has importado ya)
import pandas as pd

# Definimos el nombre del archivo (si no lo has hecho ya)
nombre_archivo = 'alquiler.csv'

# Cargamos el archivo CSV en un DataFrame
datos_alquiler = pd.read_csv(nombre_archivo, sep=';')

# --- Nuevo Paso: Obtener estadísticas descriptivas ---

# Usamos el método .describe() en nuestro DataFrame 'datos_alquiler'.
# Por defecto, .describe() calcula estadísticas solo para las columnas numéricas (int64, float64).
# Proporciona estadísticas clave como:
# - count: Número de valores no nulos (coincide con 'Non-Null Count' de .info()).
# - mean: El promedio de los valores.
# - std: La desviación estándar (qué tan dispersos están los valores).
# - min: El valor mínimo.
# - 25%, 50%, 75%: Los cuartiles (el 50% es la mediana).
# - max: El valor máximo.
# Esto nos ayuda a entender el rango típico de los valores en cada columna numérica.
print("\nEstadísticas descriptivas del DataFrame:")
print(datos_alquiler.describe())

# Si quisiéramos estadísticas de las columnas de texto ('object'),
# podemos usar include='object':
# print("\nEstadísticas descriptivas de columnas de texto:")
# print(datos_alquiler.describe(include='object'))

# Si quisiéramos estadísticas de TODAS las columnas (numéricas y de texto),
# podemos usar include='all':
# print("\nEstadísticas descriptivas de todas las columnas:")
# print(datos_alquiler.describe(include='all'))

'''
Salidas:

Estadísticas descriptivas del DataFrame:
       Habitaciones       Garages        Suites          Area         Valor    Condominio      Impuesto
count  25121.000000  25121.000000  25121.000000  25121.000000  2.510700e+04  2.249500e+04  1.803700e+04
mean       1.748856      1.798655      0.656781    220.885076  3.688505e+04  9.528676e+03  4.436513e+03
std        1.811131     22.906129      1.083180    817.465428  3.669381e+05  1.547102e+05  2.283381e+04
min        0.000000      0.000000      0.000000      0.000000  3.150000e+02  3.500000e+00  3.500000e+00
25%        0.000000      0.000000      0.000000     55.000000  5.600000e+03  2.275000e+03  4.270000e+02
50%        2.000000      1.000000      0.000000     90.000000  1.137500e+04  4.056500e+03  1.008000e+03
75%        3.000000      2.000000      1.000000    180.000000  2.695000e+04  7.350000e+03  2.625000e+03
max      100.000000   1966.000000     24.000000  42000.000000  5.250000e+07  2.293400e+07  1.577188e+06
                                                                                                         

¡Excelente! Has obtenido correctamente las estadísticas descriptivas para las columnas numéricas de tu DataFrame.

Este output del .describe() nos da una primera idea de la distribución de los datos en cada columna numérica:

count: Confirma el número de valores no nulos que ya vimos con .info(). Es útil verlo de nuevo aquí para recordar cuántos datos tenemos realmente para cada cálculo.
mean: El promedio de los valores en cada columna. Por ejemplo, el promedio de habitaciones es aproximadamente 1.75.
std: La desviación estándar. Es una medida de cuánto varían los datos respecto al promedio. Una desviación estándar alta (como en Garages, Area, Valor, Condominio, Impuesto) comparada con la media sugiere que los valores están muy dispersos, lo que podría indicar la presencia de valores extremos (outliers).
min y max: Los valores mínimo y máximo. Nos muestran el rango completo de los datos en cada columna. Notamos valores máximos muy altos en Garages, Area, Valor, Condominio e Impuesto, lo que refuerza la idea de posible presencia de outliers o propiedades de características muy diferentes al promedio.
25%, 50% (Mediana), 75%: Estos son los cuartiles. Dividen los datos en cuatro partes iguales. La mediana (50%) es el valor central. Comparar la media y la mediana es otra forma de detectar si los datos están sesgados (si la media es mucho mayor o menor que la mediana, como en Valor, suele haber valores extremos que la arrastran).
Estas estadísticas numéricas son muy informativas. Por ejemplo, vemos que el valor promedio (mean) de los alquileres es de unos $36,885, pero la mediana (50%) es solo de $11,375. Esto indica que la mayoría de los alquileres son de valores más bajos, pero hay algunos alquileres muy caros que elevan significativamente el promedio.

Ahora, para seguir explorando nuestro dataset de forma básica, es útil ver qué tipos de valores tenemos en las columnas no numéricas, como Tipo y Colonia. Queremos saber cuántos tipos de inmuebles hay y en qué colonias están ubicados.

Para esto, podemos usar dos métodos: .unique() para ver todos los valores distintos, y .value_counts() para ver cuántas veces aparece cada valor distinto.
'''