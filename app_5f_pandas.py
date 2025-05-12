'''
Ejecuta este código y experimenta con .loc[] y .iloc[]. La diferencia clave está en si usas las 
etiquetas de índice/columna (.loc) o la posición numérica (.iloc). Practica ambas, ya que son 
herramientas esenciales para acceder a cualquier parte de tus datos en pandas. ¡Es un paso muy 
importante!
'''
# Importamos pandas (si no lo has hecho ya)
import pandas as pd

# Cargamos el archivo CSV (si no lo has hecho ya)
nombre_archivo = 'alquiler.csv'
datos_alquiler = pd.read_csv(nombre_archivo, sep=';')

# --- Nuevo Paso: Selección de filas con .loc[] (basado en etiquetas) ---

# .loc[] se usa con [fila/s, columna/s]
# Si solo especificas la fila, pandas selecciona todas las columnas para esa fila.

# 1. Seleccionar una sola fila por su etiqueta de índice (en este caso, el número del índice):
# Queremos la fila con el índice 0.
fila_0 = datos_alquiler.loc[0]

# Imprimimos la fila seleccionada. El resultado es una Serie, donde el índice es el nombre de la columna.
print("\nFila con índice 0 (usando .loc):")
print(fila_0)
print("\nTipo de 'fila_0':", type(fila_0))

# 2. Seleccionar múltiples filas por sus etiquetas de índice:
# Queremos las filas con índices 1, 3 y 5. Pasamos una lista de etiquetas.
varias_filas_loc = datos_alquiler.loc[[1, 3, 5]]

# Imprimimos las filas seleccionadas. El resultado es un DataFrame.
print("\nFilas con índices 1, 3, 5 (usando .loc):")
print(varias_filas_loc)
print("\nTipo de 'varias_filas_loc':", type(varias_filas_loc))

# 3. Seleccionar un rango de filas por sus etiquetas de índice (¡el final es inclusivo con .loc!):
# Queremos las filas desde el índice 1 hasta el índice 4 (incluyendo el 4).
rango_filas_loc = datos_alquiler.loc[1:4]

# Imprimimos el rango de filas.
print("\nRango de filas de 1 a 4 (inclusive) usando .loc:")
print(rango_filas_loc)

# 4. Seleccionar filas y columnas específicas usando .loc[]:
# Podemos combinar la selección de filas y columnas.
# Queremos las filas con índices 0, 2, 4 Y solo las columnas 'Tipo' y 'Valor'.
filas_cols_loc = datos_alquiler.loc[[0, 2, 4], ['Tipo', 'Valor']]

# Imprimimos el resultado.
print("\nFilas 0, 2, 4 y columnas 'Tipo', 'Valor' usando .loc:")
print(filas_cols_loc)


# --- Nuevo Paso: Selección de filas con .iloc[] (basado en posición entera) ---

# .iloc[] se usa con [posición_fila/s, posición_columna/s]
# Se basa en la posición numérica (0-basada) de las filas y columnas.

# 1. Seleccionar una sola fila por su posición entera:
# Queremos la primera fila (posición 0).
fila_pos_0 = datos_alquiler.iloc[0]

# Imprimimos la fila seleccionada. El resultado es una Serie.
print("\nFila en posición 0 (usando .iloc):")
print(fila_pos_0)
print("\nTipo de 'fila_pos_0':", type(fila_pos_0))


# 2. Seleccionar múltiples filas por sus posiciones enteras:
# Queremos las filas en las posiciones 1, 3 y 5. Pasamos una lista de posiciones.
varias_filas_iloc = datos_alquiler.iloc[[1, 3, 5]]

# Imprimimos las filas seleccionadas. El resultado es un DataFrame.
print("\nFilas en posiciones 1, 3, 5 (usando .iloc):")
print(varias_filas_iloc)
print("\nTipo de 'varias_filas_iloc':", type(varias_filas_iloc))


# 3. Seleccionar un rango de filas por sus posiciones enteras (¡el final es exclusivo con .iloc!):
# Queremos las filas desde la posición 1 hasta la posición 4 (sin incluir la 4).
# Es decir, las filas en las posiciones 1, 2 y 3.
rango_filas_iloc = datos_alquiler.iloc[1:4]

# Imprimimos el rango de filas.
print("\nRango de filas de posición 1 a 4 (exclusivo) usando .iloc:")
print(rango_filas_iloc)

# 4. Seleccionar filas y columnas específicas usando .iloc[]:
# Podemos combinar la selección de filas y columnas por posición.
# Queremos las filas en las posiciones 0, 2, 4 Y solo las columnas en las posiciones 0 ('Tipo') y 6 ('Valor').
filas_cols_iloc = datos_alquiler.iloc[[0, 2, 4], [0, 6]]

# Imprimimos el resultado.
print("\nFilas en posiciones 0, 2, 4 y columnas en posiciones 0, 6 usando .iloc:")
print(filas_cols_iloc)

'''

Fila con índice 0 (usando .loc):
Tipo            Cocineta
Colonia          Condesa
Habitaciones           1
Garages                0
Suites                 0
Area                  40
Valor             5950.0
Condominio        1750.0
Impuesto           210.0
Name: 0, dtype: object

Tipo de 'fila_0': <class 'pandas.core.series.Series'>

Filas con índices 1, 3, 5 (usando .loc):
                 Tipo           Colonia  Habitaciones  Garages  Suites  Area    Valor  Condominio  Impuesto
1                Casa           Polanco             2        0       1   100  24500.0         NaN       NaN
3        Departamento  Centro Histórico             1        0       0    15   2800.0      1365.0      70.0
5  Casa de Condominio          Santa Fe             5        4       5   750  77000.0         NaN       NaN

Tipo de 'varias_filas_loc': <class 'pandas.core.frame.DataFrame'>

Rango de filas de 1 a 4 (inclusive) usando .loc:
                      Tipo           Colonia  Habitaciones  Garages  ...  Area    Valor  Condominio  Impuesto
1                     Casa           Polanco             2        0  ...   100  24500.0         NaN       NaN
2  Conjunto Comercial/Sala          Santa Fe             0        4  ...   150  18200.0     14070.0    3888.5
3             Departamento  Centro Histórico             1        0  ...    15   2800.0      1365.0      70.0
4             Departamento         Del Valle             1        0  ...    48   2800.0       805.0       NaN

[4 rows x 9 columns]

Filas 0, 2, 4 y columnas 'Tipo', 'Valor' usando .loc:
                      Tipo    Valor
0                 Cocineta   5950.0
2  Conjunto Comercial/Sala  18200.0
4             Departamento   2800.0

Fila en posición 0 (usando .iloc):
Tipo            Cocineta
Colonia          Condesa
Habitaciones           1
Garages                0
Suites                 0
Area                  40
Valor             5950.0
Condominio        1750.0
Impuesto           210.0
Name: 0, dtype: object

Tipo de 'fila_pos_0': <class 'pandas.core.series.Series'>

Filas en posiciones 1, 3, 5 (usando .iloc):
                 Tipo           Colonia  Habitaciones  Garages  Suites  Area    Valor  Condominio  Impuesto
1                Casa           Polanco             2        0       1   100  24500.0         NaN       NaN
3        Departamento  Centro Histórico             1        0       0    15   2800.0      1365.0      70.0
5  Casa de Condominio          Santa Fe             5        4       5   750  77000.0         NaN       NaN

Tipo de 'varias_filas_iloc': <class 'pandas.core.frame.DataFrame'>

Rango de filas de posición 1 a 4 (exclusivo) usando .iloc:
                      Tipo           Colonia  Habitaciones  Garages  ...  Area    Valor  Condominio  Impuesto
1                     Casa           Polanco             2        0  ...   100  24500.0         NaN       NaN
2  Conjunto Comercial/Sala          Santa Fe             0        4  ...   150  18200.0     14070.0    3888.5
3             Departamento  Centro Histórico             1        0  ...    15   2800.0      1365.0      70.0

[3 rows x 9 columns]

Filas en posiciones 0, 2, 4 y columnas en posiciones 0, 6 usando .iloc:
                      Tipo    Valor
0                 Cocineta   5950.0
2  Conjunto Comercial/Sala  18200.0
4             Departamento   2800.0


Explicación:

¡Excelente! Has ejecutado correctamente los ejemplos de .loc e .iloc. Ahora comprendes cómo acceder 
a tus datos tanto por su etiqueta de índice/columna como por su posición numérica. Esta es una
habilidad fundamental en pandas.

Como has visto:

Seleccionar una sola fila con .loc[etiqueta] o .iloc[posicion] te da una Serie.
Seleccionar múltiples filas (ya sea con una lista de etiquetas/posiciones o con un rango) te da un 
DataFrame.

La diferencia importante en los rangos: .loc[inicio:fin] incluye el fin, mientras 
que .iloc[inicio:fin] excluye el fin (como en las listas de Python).

Ahora que ya sabemos seleccionar columnas y filas específicas, un paso muy común e importante en el 
análisis de datos es filtrar el DataFrame para quedarnos solo con las filas que cumplen ciertas 
condiciones. Por ejemplo, podrías querer ver solo los departamentos, o solo las propiedades en una 
colonia específica, o aquellas con un valor mayor a cierto monto.

Pandas permite hacer esto de manera muy eficiente utilizando lo que se conoce como indexación 
booleana. Funciona creando una "máscara" de valores True o False del mismo tamaño que tu DataFrame 
o Serie, donde True indica que la fila cumple la condición y False indica que no. Luego, pasas esta 
máscara booleana al DataFrame para seleccionar solo las filas donde la máscara es True.
'''