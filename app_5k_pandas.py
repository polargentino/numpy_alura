# Importamos pandas (si no lo has hecho ya)
import pandas as pd

# Cargamos el archivo CSV (si no lo has hecho ya)
nombre_archivo = 'alquiler.csv'
datos_alquiler = pd.read_csv(nombre_archivo, sep=';')

# --- Manejo de valores faltantes (usamos el mismo código de antes) ---
datos_alquiler_limpio = datos_alquiler.copy()
datos_alquiler_limpio['Condominio'] = datos_alquiler_limpio['Condominio'].fillna(0)
datos_alquiler_limpio['Impuesto'] = datos_alquiler_limpio['Impuesto'].fillna(0)
mediana_valor_final = datos_alquiler_limpio['Valor'].median()
datos_alquiler_limpio['Valor'] = datos_alquiler_limpio['Valor'].fillna(mediana_valor_final)

# --- Nuevo Paso: Crear nuevas columnas ---

# Antes de crear 'Valor_por_Area', verificamos si hay Area = 0
# print("\nConteo de valores cero en la columna 'Area':")
# print((datos_alquiler_limpio['Area'] == 0).sum())
# Vemos que sí hay propiedades con Área = 0. La división por cero resultaría en Inf (infinito).
# Para manejar esto, podemos reemplazar los 0 en 'Area' por un valor pequeño o NaN,
# o simplemente ser conscientes de que los resultados para Area=0 serán infinitos o NaN si usamos fillna.
# Por ahora, vamos a permitir la división y ver los resultados (serán Inf).

# 1. Crear una nueva columna mediante un cálculo:
# Para crear una nueva columna, simplemente le asignas un nombre y le das un valor.
# Aquí, el valor es el resultado de dividir la columna 'Valor' por la columna 'Area'.
# Pandas realiza la operación elemento a elemento (para cada fila).
datos_alquiler_limpio['Valor_por_Area'] = datos_alquiler_limpio['Valor'] / datos_alquiler_limpio['Area']

# Imprimimos las primeras filas para ver la nueva columna.
print("\nDataFrame con la nueva columna 'Valor_por_Area' (primeras filas):")
print(datos_alquiler_limpio.head())

# Vemos que para las filas donde Area es 0, Valor_por_Area es 'inf' (infinito), lo cual es esperado.
# Podemos manejar estos 'inf' si queremos, por ejemplo, reemplazándolos por NaN o 0.
# Vamos a reemplazar los 'inf' resultantes de la división por NaN.
import numpy as np # Necesitamos numpy para usar np.inf
datos_alquiler_limpio['Valor_por_Area'] = datos_alquiler_limpio['Valor_por_Area'].replace([np.inf, -np.inf], np.nan)

# Ahora, si quisiéramos, podríamos rellenar estos nuevos NaNs.
# Por ejemplo, rellenarlos con 0 o con la mediana de 'Valor_por_Area' (calculada DESPUÉS de crear la columna).
# mediana_valor_por_area = datos_alquiler_limpio['Valor_por_Area'].median()
# datos_alquiler_limpio['Valor_por_Area'] = datos_alquiler_limpio['Valor_por_Area'].fillna(mediana_valor_por_area)

# 2. Crear una nueva columna basada en una condición simple:
# Supongamos que queremos una columna que indique si una propiedad es 'Grande' (Área > 200).
# Creamos una condición booleana.
es_grande = datos_alquiler_limpio['Area'] > 200

# Asignamos valores a la nueva columna 'Es_Grande' basándonos en la condición.
# Puedes asignar un valor único a la columna completa, o una Serie (como la condición booleana aquí).
datos_alquiler_limpio['Es_Grande'] = es_grande

# Imprimimos las primeras filas para ver la nueva columna booleana.
print("\nDataFrame con la nueva columna booleana 'Es_Grande' (primeras filas):")
print(datos_alquiler_limpio.head())

# Podemos ver el conteo de valores True/False en la nueva columna.
print("\nConteo de valores en la columna 'Es_Grande':")
print(datos_alquiler_limpio['Es_Grande'].value_counts())

'''

DataFrame con la nueva columna 'Valor_por_Area' (primeras filas):
                      Tipo           Colonia  Habitaciones  ...  Condominio  Impuesto  Valor_por_Area
0                 Cocineta           Condesa             1  ...      1750.0     210.0      148.750000
1                     Casa           Polanco             2  ...         0.0       0.0      245.000000
2  Conjunto Comercial/Sala          Santa Fe             0  ...     14070.0    3888.5      121.333333
3             Departamento  Centro Histórico             1  ...      1365.0      70.0      186.666667
4             Departamento         Del Valle             1  ...       805.0       0.0       58.333333

[5 rows x 10 columns]

DataFrame con la nueva columna booleana 'Es_Grande' (primeras filas):
                      Tipo           Colonia  Habitaciones  ...  Impuesto  Valor_por_Area  Es_Grande
0                 Cocineta           Condesa             1  ...     210.0      148.750000      False
1                     Casa           Polanco             2  ...       0.0      245.000000      False
2  Conjunto Comercial/Sala          Santa Fe             0  ...    3888.5      121.333333      False
3             Departamento  Centro Histórico             1  ...      70.0      186.666667      False
4             Departamento         Del Valle             1  ...       0.0       58.333333      False

[5 rows x 11 columns]

Conteo de valores en la columna 'Es_Grande':
Es_Grande
False    19638
True      5483
Name: count, dtype: int64



Explicación de Gemini:
---------------------

¡Excelente! Has creado con éxito nuevas columnas en tu DataFrame.

Lo que ves en la salida confirma:

La columna Valor_por_Area fue añadida, mostrando el resultado de dividir el valor por el área para 
cada propiedad. Los valores como 148.75, 245.0, etc., representan el costo por metro cuadrado.

La columna Es_Grande fue añadida. Contiene False para las primeras filas porque su Area es menor o 
igual a 200, y contendría True para filas donde el área es mayor a 200.

El .value_counts() de Es_Grande te muestra rápidamente cuántas propiedades en tu dataset tienen 
un área mayor a 200 (5483) y cuántas no (19638).

¡Felicidades! Has llegado a un punto donde tienes un DataFrame limpio, explorado y con nuevas 
características derivadas.

Ahora, después de realizar pasos de limpieza y transformación como los que hemos hecho (manejar 
NaNs, crear nuevas columnas), es muy común querer guardar el DataFrame resultante en un nuevo archivo. Así, puedes continuar trabajando con este DataFrame "limpio" y transformado en sesiones futuras sin tener que repetir todos los pasos de carga, limpieza y creación de columnas cada vez.

Pandas hace que esto sea muy sencillo con el método .to_csv().

Aquí tienes el código para guardar tu DataFrame datos_alquiler_limpio en un nuevo archivo CSV, con 
comentarios:


'''