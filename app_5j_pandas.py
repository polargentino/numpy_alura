# Importamos pandas (si no lo has hecho ya)
import pandas as pd

# Cargamos el archivo CSV (si no lo has hecho ya)
nombre_archivo = 'alquiler.csv'
datos_alquiler = pd.read_csv(nombre_archivo, sep=';')

# --- Manejo de valores faltantes (usamos el mismo código de antes para asegurar que partimos del mismo DataFrame limpio) ---
datos_alquiler_limpio = datos_alquiler.copy()
datos_alquiler_limpio['Condominio'] = datos_alquiler_limpio['Condominio'].fillna(0)
datos_alquiler_limpio['Impuesto'] = datos_alquiler_limpio['Impuesto'].fillna(0)
mediana_valor_final = datos_alquiler_limpio['Valor'].median()
datos_alquiler_limpio['Valor'] = datos_alquiler_limpio['Valor'].fillna(mediana_valor_final)

# --- Nuevo Paso: Ordenar datos con .sort_values() ---

# 1. Ordenar el DataFrame por una sola columna (ascendente por defecto):
# Queremos ordenar el DataFrame limpio por la columna 'Valor'.
# El método .sort_values() devuelve un nuevo DataFrame ordenado.
datos_ordenados_por_valor = datos_alquiler_limpio.sort_values(by='Valor')

# Imprimimos las primeras filas para ver los valores más bajos.
print("\nPrimeras filas del DataFrame ordenado por 'Valor' (ascendente):")
print(datos_ordenados_por_valor.head())

# 2. Ordenar el DataFrame por una sola columna (descendente):
# Usamos el argumento 'ascending=False' para ordenar de mayor a menor.
datos_ordenados_por_valor_desc = datos_alquiler_limpio.sort_values(by='Valor', ascending=False)

# Imprimimos las primeras filas para ver los valores más altos.
print("\nPrimeras filas del DataFrame ordenado por 'Valor' (descendente):")
print(datos_ordenados_por_valor_desc.head())

# 3. Ordenar el DataFrame por múltiples columnas:
# Pasamos una lista de nombres de columnas al argumento 'by'.
# Pandas ordenará primero por la primera columna de la lista, luego por la segunda, y así sucesivamente.
# Queremos ordenar primero por 'Habitaciones' (ascendente) y luego por 'Valor' (descendente) dentro de cada número de habitaciones.
datos_ordenados_multiple = datos_alquiler_limpio.sort_values(by=['Habitaciones', 'Valor'], ascending=[True, False])

# Imprimimos las primeras filas.
print("\nPrimeras filas del DataFrame ordenado por 'Habitaciones' (asc) y 'Valor' (desc):")
print(datos_ordenados_multiple.head())

# 4. Ordenar los resultados de una agregación:
# Podemos aplicar .sort_values() directamente al resultado de un .groupby().mean().
# Ya teníamos el promedio de Valor, Condominio, Impuesto por Tipo:
agrupado_por_tipo = datos_alquiler_limpio.groupby('Tipo')
promedio_valor_condominio_impuesto_por_tipo = agrupado_por_tipo[['Valor', 'Condominio', 'Impuesto']].mean()

# Ahora ordenamos este resultado por la columna 'Valor' (descendente) para ver qué tipos tienen el valor promedio más alto.
promedio_ordenado_por_valor = promedio_valor_condominio_impuesto_por_tipo.sort_values(by='Valor', ascending=False)

print("\nPromedio de Valor, Condominio, Impuesto por Tipo, ordenado por 'Valor' (descendente):")
print(promedio_ordenado_por_valor)

# También podemos ordenar por el índice (el nombre del Tipo, en este caso)
# promedio_ordenado_por_tipo_nombre = promedio_valor_condominio_impuesto_por_tipo.sort_index()
# print("\nPromedio de Valor, Condominio, Impuesto por Tipo, ordenado por nombre del Tipo:")
# print(promedio_ordenado_por_tipo_nombre)

'''

Primeras filas del DataFrame ordenado por 'Valor' (ascendente):
                          Tipo           Colonia  Habitaciones  Garages  ...  Area  Valor  Condominio  Impuesto
6574   Conjunto Comercial/Sala        La Condesa             0        7  ...  1628  315.0        45.5       0.0
16446  Cochera/Estacionamiento  Centro Histórico             0        0  ...     0  315.0         0.0     304.5
6344              Departamento           Condesa             0        0  ...    15  350.0         0.0       0.0
398    Cochera/Estacionamiento  Centro Histórico             0        1  ...     0  350.0         0.0       0.0
9964              Departamento          Santa Fe             0        0  ...    15  350.0         0.0       0.0

[5 rows x 9 columns]

Primeras filas del DataFrame ordenado por 'Valor' (descendente):
                          Tipo                 Colonia  Habitaciones  ...       Valor  Condominio  Impuesto
3463   Galpón/Depósito/Almacén               Nativitas             0  ...  52500000.0         0.0    3500.0
17818             Departamento                    Roma             4  ...  15750000.0      3850.0       0.0
19510        Edificio Completo  San Pedro de los Pinos             0  ...   4636240.0    579530.0  339111.5
20048  Conjunto Comercial/Sala          San Juan Xalpa             0  ...   4477200.0         0.0       0.0
21380        Edificio Completo  San Pedro de los Pinos             0  ...   3766945.0         0.0       0.0

[5 rows x 9 columns]

Primeras filas del DataFrame ordenado por 'Habitaciones' (asc) y 'Valor' (desc):
                          Tipo                 Colonia  Habitaciones  ...       Valor  Condominio  Impuesto
3463   Galpón/Depósito/Almacén               Nativitas             0  ...  52500000.0         0.0    3500.0
19510        Edificio Completo  San Pedro de los Pinos             0  ...   4636240.0    579530.0  339111.5
20048  Conjunto Comercial/Sala          San Juan Xalpa             0  ...   4477200.0         0.0       0.0
21380        Edificio Completo  San Pedro de los Pinos             0  ...   3766945.0         0.0       0.0
19619        Edificio Completo        Centro Histórico             0  ...   3325000.0         0.0  159278.0

[5 rows x 9 columns]

Promedio de Valor, Condominio, Impuesto por Tipo, ordenado por 'Valor' (descendente):
                                    Valor    Condominio      Impuesto
Tipo                                                                 
Industria                   420000.000000      0.000000      0.000000
Edificio Completo           409418.080645  24834.129032  27646.241935
Galpón/Depósito/Almacén     299984.140138   5547.330450  13710.638408
Terreno Estándar            135364.444444      0.000000  15548.555556
Loteo/Condominio             92166.666667      0.000000  17097.500000
Hotel                        87500.000000      0.000000  21707.000000
Conjunto Comercial/Sala      57642.614504  16605.811301   3819.485126
Tienda/Salón                 56181.780055   6409.606102   6791.428051
Casa Comercial               54735.841584    981.074257   4334.559406
Casa de Condominio           51428.609836   4783.920492  11396.206557
Rancho                       38014.375000      0.000000   1093.750000
Tienda en Centro Comercial   32449.263959   5819.593909   3562.022843
Casa                         31453.177064    909.582569   3259.964220
Departamento                 18679.804389   6570.124187   1957.273063
Departamento en Hotel        16285.430769   6613.230769   1481.230769
Loft                          9924.526316   3224.789474    723.671053
Estudio                       8400.000000    960.750000    529.375000
Cochera/Estacionamiento       6995.454545    277.681818    140.090909
Casa de Vecindad              5961.740506    164.854430    313.161392
Posada/Chalé                  5180.000000   1032.500000      0.000000
Cocineta                      4425.856061   1427.411846    185.201102


Explicación de Gemini:
---------------------

¡Excelente! Has practicado la ordenación de datos con .sort_values() de manera efectiva.

Como puedes ver:

Ordenar el DataFrame por Valor (ascendente y descendente) te permite identificar rápidamente las propiedades más baratas y más caras en el dataset. Los valores máximos confirman los posibles "outliers" que sospechábamos al ver el .describe().
Ordenar por múltiples columnas te da un control más fino sobre la organización de tus datos.
Ordenar el resultado de la agrupación por Tipo y Valor promedio (promedio_ordenado_por_valor) es muy ilustrativo. Ahora puedes ver fácilmente que Industria, Edificio Completo y Galpón/Depósito/Almacén son los tipos de inmuebles con los valores de alquiler promedio más altos, mientras que Cocineta, Casa de Vecindad y Posada/Chalé tienen los promedios más bajos.
Ya hemos cubierto la carga, inspección, selección, filtrado, limpieza básica y agrupación/agregación de datos.

Un paso muy común en el análisis de datos es crear nuevas columnas en tu DataFrame. Esto te permite derivar nueva información o características a partir de las columnas existentes, lo que puede ser muy útil para análisis posteriores o para crear visualizaciones más significativas.

Podemos crear una nueva columna de varias maneras, por ejemplo:

Realizando cálculos con columnas existentes.
Aplicando una función a una columna o a varias columnas.
Basándonos en condiciones lógicas.
Vamos a empezar creando una nueva columna simple: el valor de alquiler por metro cuadrado (Valor_por_Area). Esto nos dará una medida estandarizada del precio que puede ser más comparable entre propiedades de diferentes tamaños.

Antes de dividir, es buena práctica verificar si la columna por la que vamos a dividir (Area) contiene ceros para evitar errores de división por cero. Ya vimos en .describe() que el mínimo de Area es 0.
'''