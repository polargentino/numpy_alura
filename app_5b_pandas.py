'''
Al ejecutar este código, verás información sobre cuántas entradas (filas) tiene tu DataFrame, 
cuántas columnas, el nombre de cada columna, cuántos valores no son nulos en cada columna (
esto te ayuda a ver dónde faltan datos) y qué tipo de datos pandas ha inferido para cada columna 
(números enteros, números decimales, texto, etc.).

¡Este es un paso crucial para entender la "salud" de tus datos antes de profundizar en el análisis! 
Ejecuta este código y veamos qué nos dice sobre tu archivo alquiler.csv.
'''

# Importamos la librería pandas (si no la has importado ya en tu script)
import pandas as pd

# Definimos el nombre del archivo (si no lo has hecho ya)
nombre_archivo = 'alquiler.csv'

# Cargamos el archivo CSV en un DataFrame, especificando el separador ';'
datos_alquiler = pd.read_csv(nombre_archivo, sep=';')

# --- Nuevo Paso: Inspeccionar la información del DataFrame ---

# Usamos el método .info() en nuestro DataFrame 'datos_alquiler'.
# Este método imprime un resumen de la información del DataFrame, incluyendo:
# - El rango de índices (cuántas filas tiene).
# - El número total de columnas.
# - Una lista de cada columna, con:
#   - El nombre de la columna.
#   - El número de valores no nulos (non-null count) en esa columna.
#   - El tipo de dato (dtype) de los valores en la columna (por ejemplo, int64, float64, object).
# Es una herramienta muy útil para tener una visión rápida del estado de los datos.
print("Información del DataFrame:")
datos_alquiler.info()

# También podemos obtener solo la forma (dimensiones) del DataFrame.
# El atributo .shape devuelve una tupla donde el primer elemento es el número de filas
# y el segundo elemento es el número de columnas.
print("\nForma del DataFrame (filas, columnas):")
print(datos_alquiler.shape)

# Volvemos a imprimir el head para recordarnos cómo se ven los datos (opcional)
# print("\nPrimeras filas del DataFrame:")
# print(datos_alquiler.head())

'''
Sálidas: 

Información del DataFrame:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 25121 entries, 0 to 25120
Data columns (total 9 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Tipo          25121 non-null  object 
 1   Colonia       25121 non-null  object 
 2   Habitaciones  25121 non-null  int64  
 3   Garages       25121 non-null  int64  
 4   Suites        25121 non-null  int64  
 5   Area          25121 non-null  int64  
 6   Valor         25107 non-null  float64
 7   Condominio    22495 non-null  float64
 8   Impuesto      18037 non-null  float64
dtypes: float64(3), int64(4), object(2)
memory usage: 1.7+ MB

Forma del DataFrame (filas, columnas):
(25121, 9)

Respuesta de Gemini 2.5 Flash:

Perfecto! Este output de .info() y .shape nos da una radiografía muy útil de nuestro DataFrame.

Vamos a interpretar lo que nos muestra:

<class 'pandas.core.frame.DataFrame'>: Confirma que datos_alquiler es, efectivamente, un DataFrame de pandas.
RangeIndex: 25121 entries, 0 to 25120: Nos dice que el DataFrame tiene 25121 filas, con índices numéricos que van desde 0 hasta 25120. ¡Es un dataset bastante grande!
Data columns (total 9 columns):: Nos confirma que tenemos 9 columnas.
La tabla debajo (#, Column, Non-Null Count, Dtype):
Column: Los nombres de tus columnas, tal cual los leímos del CSV.
Non-Null Count: Esto es muy importante. Te dice cuántas filas no tienen un valor faltante (NaN) para esa columna.
Tipo, Colonia, Habitaciones, Garages, Suites, Area: Tienen 25121 valores no nulos, lo que significa que no les faltan datos en ninguna fila. ¡Están completos!
Valor: Tiene 25107 valores no nulos. Esto significa que faltan 25121 - 25107 = 14 valores en la columna Valor.
Condominio: Tiene 22495 valores no nulos. Faltan 25121 - 22495 = 2626 valores.
Impuesto: Tiene 18037 valores no nulos. Faltan 25121 - 18037 = 7084 valores. Ya identificamos columnas con datos faltantes (Valor, Condominio, Impuesto), lo cual es un paso clave en la limpieza de datos.
Dtype: El tipo de dato que pandas ha asignado a cada columna:
object: Típicamente strings (texto), como los nombres de Tipo y Colonia.
int64: Números enteros, como Habitaciones, Garages, Suites, Area.
float64: Números decimales (de punto flotante), como Valor, Condominio, Impuesto. Es lógico que sean float porque pueden tener valores con decimales o porque pandas los representa así cuando hay valores faltantes (NaN).
dtypes: float64(3), int64(4), object(2): Un resumen general de cuántas columnas hay de cada tipo de dato.
memory usage: 1.7+ MB: Una estimación de cuánta memoria RAM ocupa el DataFrame.
Forma del DataFrame (filas, columnas): (25121, 9): Nos confirma directamente el número de filas y columnas, que coincide con la información de RangeIndex y Data columns.
Ahora que conocemos la estructura de los datos y hemos identificado las columnas con valores faltantes, el siguiente paso lógico en la exploración inicial es obtener estadísticas descriptivas de las columnas numéricas. Esto nos da una idea de la distribución de los valores (promedio, valores mínimos y máximos, etc.).

Podemos usar el método .describe() para esto.

Aquí tienes el código:


'''