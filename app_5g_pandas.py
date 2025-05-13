# Importamos pandas (si no lo has hecho ya)
import pandas as pd

# Cargamos el archivo CSV (si no lo has hecho ya)
nombre_archivo = 'alquiler.csv'
datos_alquiler = pd.read_csv(nombre_archivo, sep=';')

# --- Nuevo Paso: Filtrar filas basadas en condiciones ---

# 1. Crear una condición simple:
# Queremos seleccionar solo las filas donde el 'Tipo' de inmueble es 'Departamento'.
# Al aplicar una condición a una columna (una Serie), el resultado es una Serie de valores True/False.
# Cada True corresponde a una fila donde la condición es cierta.
condicion_departamento = datos_alquiler['Tipo'] == 'Departamento'

# Imprimimos las primeras filas de esta Serie booleana para verla.
print("\nPrimeras filas de la condición 'Tipo == Departamento':")
print(condicion_departamento.head())
# Nota que esta Serie booleana tiene el mismo índice que el DataFrame original.

# 2. Usar la condición para filtrar el DataFrame:
# Pasamos la Serie booleana (la condición) dentro de los corchetes [] del DataFrame.
# Pandas devolverá un nuevo DataFrame que contiene solo las filas donde la condición fue True.
solo_departamentos = datos_alquiler[condicion_departamento]

# Imprimimos las primeras filas del DataFrame filtrado.
print("\nPrimeras filas del DataFrame filtrado (solo Departamentos):")
print(solo_departamentos.head())

# O de forma más directa, aplicando la condición directamente dentro de los corchetes:
# solo_departamentos_directo = datos_alquiler[datos_alquiler['Tipo'] == 'Departamento']
# print("\nPrimeras filas del DataFrame filtrado (directo):")
# print(solo_departamentos_directo.head())


# 3. Filtrar usando una condición numérica:
# Queremos seleccionar solo las propiedades con más de 2 habitaciones.
condicion_habitaciones = datos_alquiler['Habitaciones'] > 2

# Aplicamos la condición para filtrar.
propiedades_mas_de_2_habitaciones = datos_alquiler[condicion_habitaciones]

print("\nPrimeras filas de propiedades con más de 2 habitaciones:")
print(propiedades_mas_de_2_habitaciones.head())


# 4. Combinar múltiples condiciones:
# Podemos combinar condiciones usando operadores lógicos:
# - '&' para AND (ambas condiciones deben ser True)
# - '|' para OR (al menos una condición debe ser True)
# - '~' para NOT (la condición debe ser False)

# Queremos seleccionar solo los 'Departamento' que tienen más de 2 'Habitaciones'.
# Es importante poner cada condición entre paréntesis () cuando las combinas.
condicion_combinada = (datos_alquiler['Tipo'] == 'Departamento') & (datos_alquiler['Habitaciones'] > 2)

# Aplicamos las condiciones combinadas para filtrar.
departamentos_grandes = datos_alquiler[condicion_combinada]

print("\nPrimeras filas de Departamentos con más de 2 habitaciones:")
print(departamentos_grandes.head())

# 5. Filtrar usando el operador lógico OR (|):
# Queremos seleccionar propiedades que sean 'Casa' O 'Casa de Condominio'.
condicion_or = (datos_alquiler['Tipo'] == 'Casa') | (datos_alquiler['Tipo'] == 'Casa de Condominio')

casas = datos_alquiler[condicion_or]

print("\nPrimeras filas de Casas o Casas de Condominio:")
print(casas.head())

'''
Primeras filas de la condición 'Tipo == Departamento':
0    False
1    False
2    False
3     True
4     True
Name: Tipo, dtype: bool

Primeras filas del DataFrame filtrado (solo Departamentos):
            Tipo           Colonia  Habitaciones  Garages  Suites  Area    Valor  Condominio  Impuesto
3   Departamento  Centro Histórico             1        0       0    15   2800.0      1365.0      70.0
4   Departamento         Del Valle             1        0       0    48   2800.0       805.0       NaN
7   Departamento  Centro Histórico             1        0       0    36   4200.0         NaN       NaN
8   Departamento           Condesa             1        0       1    40   7000.0      1963.5     175.0
10  Departamento           Condesa             4        3       1   243  45500.0      7000.0    2810.5

Primeras filas de propiedades con más de 2 habitaciones:
                     Tipo   Colonia  Habitaciones  Garages  Suites  Area    Valor  Condominio  Impuesto
5      Casa de Condominio  Santa Fe             5        4       5   750  77000.0         NaN       NaN
10           Departamento   Condesa             4        3       1   243  45500.0      7000.0    2810.5
12  Departamento en Hotel      Roma             3        1       1    80  13300.0      3640.0       NaN
15     Casa de Condominio  Santa Fe             4        3       2   466  26250.0      9432.5       NaN
18           Departamento  Coyoacán             3        1       1   125  24500.0      7350.0    1620.5

Primeras filas de Departamentos con más de 2 habitaciones:
            Tipo   Colonia  Habitaciones  Garages  Suites  Area    Valor  Condominio  Impuesto
10  Departamento   Condesa             4        3       1   243  45500.0      7000.0    2810.5
18  Departamento  Coyoacán             3        1       1   125  24500.0      7350.0    1620.5
20  Departamento  Santa Fe             3        3       1   175  14700.0      5250.0    1750.0
22  Departamento   Condesa             3        1       2   378  35000.0      7525.0    2450.0
23  Departamento   Condesa             3        0       0   180  19250.0      6230.0    1470.0

Primeras filas de Casas o Casas de Condominio:
                  Tipo     Colonia  Habitaciones  Garages  Suites  Area    Valor  Condominio  Impuesto
1                 Casa     Polanco             2        0       1   100  24500.0         NaN       NaN
5   Casa de Condominio    Santa Fe             5        4       5   750  77000.0         NaN       NaN
15  Casa de Condominio    Santa Fe             4        3       2   466  26250.0      9432.5       NaN
41  Casa de Condominio    Santa Fe             5       10       5  1600  87500.0      5600.0       NaN
96                Casa  Lindavista             1        0       0    33   4200.0         NaN       NaN



Explicación de Gemini:
---------------------

¡Excelente! Has comprendido muy bien cómo funciona el filtrado de datos utilizando condiciones 
booleanas. Como puedes ver en la salida, al aplicar una condición, obtienes un sub-DataFrame que 
contiene solo las filas que cumplen esa condición. Combinar condiciones con & (AND) y | (OR) te 
permite realizar filtros más específicos.

Ya hemos cargado los datos, explorado su estructura (.info(), .shape), visto estadísticas básicas 
(.describe()) y aprendido a seleccionar y filtrar datos.

Ahora, recordemos que al usar .info(), identificamos que las columnas Valor, Condominio e Impuesto 
tienen valores faltantes (NaN). Trabajar con datos faltantes es un paso crucial en la limpieza de 
datos, ya que pueden afectar los análisis posteriores.

El siguiente paso es aprender a identificar y manejar estos valores faltantes. Pandas nos proporciona 
herramientas muy útiles para esto.
'''