'''
Ejecuta este código. Verás cómo puedes extraer fácilmente columnas específicas para trabajar con 
ellas por separado o crear sub-DataFrames con solo la información que necesitas en un momento dado.

¡Este es un concepto fundamental para manipular datos con pandas! Después de esto, podemos pasar a 
seleccionar filas o incluso a filtrar datos según condiciones. ¡Sigamos avanzando!
'''
# Importamos pandas (si no lo has hecho ya)
import pandas as pd

# Cargamos el archivo CSV (si no lo has hecho ya)
nombre_archivo = 'alquiler.csv'
datos_alquiler = pd.read_csv(nombre_archivo, sep=';')

# --- Nuevo Paso: Selección de columnas ---

# 1. Seleccionar una sola columna:
# Para seleccionar una columna, usamos corchetes [] y el nombre de la columna como un string.
# El resultado es una Serie de pandas, que es como un arreglo unidimensional con un índice.
# Vamos a seleccionar la columna 'Valor'.
valores_alquiler = datos_alquiler['Valor']

# Imprimimos las primeras filas de esta Serie para ver su contenido.
print("\nPrimeras filas de la columna 'Valor':")
print(valores_alquiler.head())

# También podemos imprimir su tipo para confirmar que es una Serie.
print("\nTipo de 'valores_alquiler':")
print(type(valores_alquiler))

# 2. Seleccionar múltiples columnas:
# Para seleccionar varias columnas, usamos doble corchete [[]] y una lista de nombres
# de columnas como strings dentro.
# El resultado es un nuevo DataFrame que contiene solo las columnas seleccionadas.
# Vamos a seleccionar las columnas 'Tipo', 'Colonia' y 'Valor'.
propiedades_ubicacion_valor = datos_alquiler[['Tipo', 'Colonia', 'Valor']]

# Imprimimos las primeras filas de este nuevo DataFrame.
print("\nPrimeras filas del DataFrame con 'Tipo', 'Colonia', 'Valor':")
print(propiedades_ubicacion_valor.head())

# Y confirmamos su tipo para ver que es un DataFrame.
print("\nTipo de 'propiedades_ubicacion_valor':")
print(type(propiedades_ubicacion_valor))

'''
Primeras filas de la columna 'Valor':
0     5950.0
1    24500.0
2    18200.0
3     2800.0
4     2800.0
Name: Valor, dtype: float64

Tipo de 'valores_alquiler':
<class 'pandas.core.series.Series'>

Primeras filas del DataFrame con 'Tipo', 'Colonia', 'Valor':
                      Tipo           Colonia    Valor
0                 Cocineta           Condesa   5950.0
1                     Casa           Polanco  24500.0
2  Conjunto Comercial/Sala          Santa Fe  18200.0
3             Departamento  Centro Histórico   2800.0
4             Departamento         Del Valle   2800.0

Tipo de 'propiedades_ubicacion_valor':
<class 'pandas.core.frame.DataFrame'>

Explicación de Gemini: 
---------------------

¡Excelente! Has dominado la selección de columnas con éxito. Como ves, obtener una columna te da una 
Serie y obtener múltiples columnas te da otro DataFrame. Esto es un concepto clave en pandas.

Ahora que sabemos cómo seleccionar columnas, el siguiente paso lógico es aprender a seleccionar filas 
específicas de nuestro DataFrame. A veces necesitamos analizar solo ciertas observaciones o registros.

Pandas ofrece dos formas principales de seleccionar filas (o una combinación de filas y columnas):

.loc[]: Se basa en etiquetas (labels) del índice y/o nombres de columnas.
.iloc[]: Se basa en la posición entera (integer location) de las filas y columnas (como en los 
arreglos de Python, empezando desde 0).
'''