# Importamos pandas (si no lo has hecho ya)
import pandas as pd

# Cargamos el archivo CSV (si no lo has hecho ya)
nombre_archivo = 'alquiler.csv'
datos_alquiler = pd.read_csv(nombre_archivo, sep=';')

# --- Nuevo Paso: Identificar y manejar valores faltantes (NaN) ---

# 1. Identificar dónde están los valores faltantes:
# El método .isnull() devuelve un DataFrame booleano del mismo tamaño que el original,
# donde True indica una celda con valor faltante (NaN).
print("\nDataFrame booleano indicando valores nulos (primeras filas):")
print(datos_alquiler.isnull().head())

# El método .notnull() hace lo contrario, True indica valores no nulos.
# print("\nDataFrame booleano indicando valores no nulos (primeras filas):")
# print(datos_alquiler.notnull().head())

# Para obtener el conteo total de valores faltantes por columna, podemos encadenar .isnull() con .sum().
# Como True se evalúa como 1 y False como 0 en operaciones numéricas, .sum() cuenta los True.
print("\nConteo de valores nulos por columna:")
print(datos_alquiler.isnull().sum())

# Este conteo coincide con la diferencia entre el total de filas (.shape[0])
# y los 'Non-Null Count' que vimos en .info().

# 2. Manejar valores faltantes - Opción 1: Eliminar filas con NaN
# El método .dropna() elimina las filas que contienen al menos un valor faltante.
# Esto puede ser útil si pierdes pocos datos, pero puede resultar en una pérdida significativa si hay muchos NaNs.
# El argumento 'inplace=True' modifica el DataFrame original (úsalo con precaución).
# Si no usas inplace=True, devuelve un nuevo DataFrame sin los NaNs.
datos_alquiler_sin_nan = datos_alquiler.dropna()

print("\nDimensiones del DataFrame original:", datos_alquiler.shape)
print("Dimensiones del DataFrame después de eliminar filas con NaN:", datos_alquiler_sin_nan.shape)

# Podemos ver las primeras filas del nuevo DataFrame para confirmar que se eliminaron las filas con NaN.
# print("\nPrimeras filas del DataFrame después de eliminar filas con NaN:")
# print(datos_alquiler_sin_nan.head())

# 3. Manejar valores faltantes - Opción 2: Rellenar valores faltantes
# El método .fillna() reemplaza los valores faltantes (NaN) por un valor especificado.
# Hay varias estrategias para rellenar NaNs:

# a) Rellenar con un valor fijo (por ejemplo, 0):
# Esto puede ser adecuado para columnas como 'Condominio' o 'Impuesto' si asumimos que NaN significa que no aplica o es 0.
# Creamos una copia para no modificar el DataFrame original todavía.
datos_alquiler_rellenado_0 = datos_alquiler.fillna(0)

print("\nConteo de valores nulos después de rellenar con 0:")
print(datos_alquiler_rellenado_0.isnull().sum()) # Deberían ser 0 NaNs

# b) Rellenar con la media o la mediana de la columna:
# Esto es común para columnas numéricas donde la media o mediana es una estimación razonable.
# Usamos la mediana porque es menos sensible a outliers que la media.
# Rellenamos los NaNs en la columna 'Valor' con la mediana de esa columna.
mediana_valor = datos_alquiler['Valor'].median()
datos_alquiler_rellenado_mediana_valor = datos_alquiler['Valor'].fillna(mediana_valor)

# Nota: fillna() aquí solo afectó a la Serie 'Valor'. Si quieres modificar el DataFrame, puedes hacer:
datos_alquiler_rellenado_mediana = datos_alquiler.copy() # Hacemos una copia del DataFrame completo
datos_alquiler_rellenado_mediana['Valor'] = datos_alquiler_rellenado_mediana['Valor'].fillna(mediana_valor)

print("\nConteo de valores nulos en 'Valor' después de rellenar con la mediana:")
print(datos_alquiler_rellenado_mediana['Valor'].isnull().sum()) # Debería ser 0

# Podemos aplicar diferentes estrategias a diferentes columnas.
# Por ejemplo, rellenar 'Condominio' e 'Impuesto' con 0, y 'Valor' con la mediana.
datos_alquiler_limpio = datos_alquiler.copy()
datos_alquiler_limpio['Condominio'] = datos_alquiler_limpio['Condominio'].fillna(0)
datos_alquiler_limpio['Impuesto'] = datos_alquiler_limpio['Impuesto'].fillna(0)
mediana_valor_final = datos_alquiler_limpio['Valor'].median() # Calculamos la mediana DE NUEVO por si rellenar otras cols afectó
datos_alquiler_limpio['Valor'] = datos_alquiler_limpio['Valor'].fillna(mediana_valor_final)


print("\nConteo final de valores nulos después de varias estrategias de relleno:")
print(datos_alquiler_limpio.isnull().sum()) # Deberían ser 0 en Valor, Condominio, Impuesto

# Mostramos las primeras filas del DataFrame "limpio"
print("\nPrimeras filas del DataFrame después de rellenar NaNs:")
print(datos_alquiler_limpio.head())

'''
DataFrame booleano indicando valores nulos (primeras filas):
    Tipo  Colonia  Habitaciones  Garages  Suites   Area  Valor  Condominio  Impuesto
0  False    False         False    False   False  False  False       False     False
1  False    False         False    False   False  False  False        True      True
2  False    False         False    False   False  False  False       False     False
3  False    False         False    False   False  False  False       False     False
4  False    False         False    False   False  False  False       False      True

Conteo de valores nulos por columna:
Tipo               0
Colonia            0
Habitaciones       0
Garages            0
Suites             0
Area               0
Valor             14
Condominio      2626
Impuesto        7084
dtype: int64

Dimensiones del DataFrame original: (25121, 9)
Dimensiones del DataFrame después de eliminar filas con NaN: (17000, 9)

Conteo de valores nulos después de rellenar con 0:
Tipo            0
Colonia         0
Habitaciones    0
Garages         0
Suites          0
Area            0
Valor           0
Condominio      0
Impuesto        0
dtype: int64

Conteo de valores nulos en 'Valor' después de rellenar con la mediana:
0

Conteo final de valores nulos después de varias estrategias de relleno:
Tipo            0
Colonia         0
Habitaciones    0
Garages         0
Suites          0
Area            0
Valor           0
Condominio      0
Impuesto        0
dtype: int64

Primeras filas del DataFrame después de rellenar NaNs:
                      Tipo           Colonia  Habitaciones  Garages  ...  Area    Valor  Condominio  Impuesto
0                 Cocineta           Condesa             1        0  ...    40   5950.0      1750.0     210.0
1                     Casa           Polanco             2        0  ...   100  24500.0         0.0       0.0
2  Conjunto Comercial/Sala          Santa Fe             0        4  ...   150  18200.0     14070.0    3888.5
3             Departamento  Centro Histórico             1        0  ...    15   2800.0      1365.0      70.0
4             Departamento         Del Valle             1        0  ...    48   2800.0       805.0       0.0

[5 rows x 9 columns]



Explicación de Gemini:
---------------------

¡Excelente! Has completado exitosamente el manejo de los valores faltantes.

El output muestra claramente:

La matriz booleana con datos_alquiler.isnull().head() te permite visualizar dónde empiezan a aparecer 
los valores NaN en las primeras filas.

datos_alquiler.isnull().sum() te da el conteo preciso de cuántos NaN hay en cada columna. 
Esto confirma que Valor, Condominio e Impuesto son las columnas afectadas.

La diferencia de dimensiones al usar .dropna() es muy notoria: pasas de 25121 filas a 17000. Esto 
ilustra la cantidad de datos que se pierden al simplemente eliminar filas con NaNs. Por eso, rellenar 
suele ser una mejor estrategia si la pérdida de datos es muy grande.

Los conteos de nulos después de usar fillna(0) y la combinación de fillna(0) con fillna(mediana) 
muestran que lograste eliminar todos los valores faltantes en las columnas objetivo, como se confirma 
en el Conteo final.

Finalmente, el head() del DataFrame datos_alquiler_limpio muestra que donde antes había NaN 
(como en la fila 1 de Condominio e Impuesto, y la fila 4 de Impuesto), ahora hay 0.0, y el valor 
faltante en Valor también habrá sido reemplazado por la mediana calculada.

¡Ahora tienes un DataFrame "limpio" en cuanto a valores faltantes en esas columnas, listo para 
análisis más robustos!

Ya sabemos leer, inspeccionar, seleccionar, filtrar y limpiar datos básicos. Un siguiente paso muy 
común e informativo es agrupar datos por categorías y calcular estadísticas resumidas para cada grupo. Por ejemplo, podríamos querer saber cuál es el valor promedio de alquiler para cada tipo de inmueble, o para cada colonia.

Pandas tiene un método muy potente para esto: .groupby(). Funciona de la siguiente manera:

Dividir los datos en grupos basándose en los valores de una o más columnas categóricas.
Aplicar una función de agregación (como la media, suma, conteo, etc.) a las columnas numéricas dentro 
de cada grupo.

Combinar los resultados en una estructura de datos nueva.
Vamos a usar el DataFrame datos_alquiler_limpio (el que tiene los NaNs manejados) para agrupar por 
Tipo y calcular el promedio de Valor, Condominio e Impuesto para cada tipo.


'''