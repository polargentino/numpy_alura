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
# Verificamos que no hay NaNs en las columnas tratadas:
# print("\nVerificación de NaNs antes de agrupar:")
# print(datos_alquiler_limpio[['Valor', 'Condominio', 'Impuesto']].isnull().sum())

# --- Nuevo Paso: Agrupar datos y agregar estadísticas ---

# 1. Agrupar por la columna 'Tipo':
# Usamos .groupby() en el DataFrame y le pasamos el nombre de la columna por la que queremos agrupar.
# Esto crea un objeto 'GroupBy', que no muestra los datos agrupados directamente,
# sino que está listo para que le apliquemos una función de agregación.
agrupado_por_tipo = datos_alquiler_limpio.groupby('Tipo')

# Imprimimos el objeto GroupBy (solo para ver qué es, no los datos agrupados)
print("\nObjeto GroupBy (agrupado por Tipo):")
print(agrupado_por_tipo)

# 2. Aplicar una función de agregación (por ejemplo, la media):
# Después de agrupar, aplicamos una función de agregación al objeto GroupBy.
# Pandas calculará la media para CADA columna numérica, para CADA grupo ('Tipo').
promedio_por_tipo = agrupado_por_tipo.mean(numeric_only=True) # numeric_only=True para evitar advertencias si hay columnas no numéricas

# Imprimimos el resultado. El índice del nuevo DataFrame es la columna por la que agrupamos ('Tipo').
# Las columnas son las columnas numéricas originales, con los valores promediados para cada tipo.
print("\nPromedio de valores numéricos por Tipo de inmueble:")
print(promedio_por_tipo)

# 3. Seleccionar columnas específicas después de agrupar:
# A menudo, solo nos interesan las estadísticas de ciertas columnas.
# Podemos seleccionar las columnas de interés DESPUÉS de aplicar la función de agregación.
promedio_valor_condominio_impuesto_por_tipo = agrupado_por_tipo[['Valor', 'Condominio', 'Impuesto']].mean()

print("\nPromedio de Valor, Condominio e Impuesto por Tipo de inmueble:")
print(promedio_valor_condominio_impuesto_por_tipo)

# 4. Agrupar por múltiples columnas:
# Podemos agrupar por más de una columna pasando una lista de nombres de columnas a groupby().
# Por ejemplo, agrupar por 'Colonia' y 'Tipo'.
agrupado_por_colonia_tipo = datos_alquiler_limpio.groupby(['Colonia', 'Tipo'])

# Y calcular la media para cada combinación de Colonia y Tipo.
promedio_por_colonia_tipo = agrupado_por_colonia_tipo[['Valor']].mean() # Solo queremos el promedio del Valor

print("\nPromedio de Valor por Colonia y Tipo (primeras filas):")
print(promedio_por_colonia_tipo.head())

'''

Objeto GroupBy (agrupado por Tipo):
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x7f05211990f0>

Promedio de valores numéricos por Tipo de inmueble:
                            Habitaciones    Garages     Suites  ...          Valor    Condominio      Impuesto
Tipo                                                            ...                                           
Casa                            3.359633   1.897248   1.438532  ...   31453.177064    909.582569   3259.964220
Casa Comercial                  1.801980   2.118812   0.257426  ...   54735.841584    981.074257   4334.559406
Casa de Condominio              4.319672   3.555738   3.247541  ...   51428.609836   4783.920492  11396.206557
Casa de Vecindad                1.974684   0.379747   0.215190  ...    5961.740506    164.854430    313.161392
Cochera/Estacionamiento         0.064935   1.376623   0.000000  ...    6995.454545    277.681818    140.090909
Cocineta                        0.836088   0.020661   0.041322  ...    4425.856061   1427.411846    185.201102
Conjunto Comercial/Sala         0.047175   2.686323   0.000352  ...   57642.614504  16605.811301   3819.485126
Departamento                    2.504199   1.256367   0.891899  ...   18679.804389   6570.124187   1957.273063
Departamento en Hotel           1.419780   0.969231   0.758242  ...   16285.430769   6613.230769   1481.230769
Edificio Completo               0.405530  11.175115   0.027650  ...  409418.080645  24834.129032  27646.241935
Estudio                         0.500000   0.250000   0.000000  ...    8400.000000    960.750000    529.375000
Galpón/Depósito/Almacén         0.069204   5.311419   0.000000  ...  299984.140138   5547.330450  13710.638408
Hotel                          25.500000   2.500000  12.000000  ...   87500.000000      0.000000  21707.000000
Industria                       0.000000   0.000000   0.000000  ...  420000.000000      0.000000      0.000000
Loft                            1.078947   0.552632   0.421053  ...    9924.526316   3224.789474    723.671053
Loteo/Condominio                0.000000   0.000000   0.000000  ...   92166.666667      0.000000  17097.500000
Posada/Chalé                   23.000000   0.000000  23.000000  ...    5180.000000   1032.500000      0.000000
Rancho                          5.125000   0.000000   3.750000  ...   38014.375000      0.000000   1093.750000
Terreno Estándar                0.066667   0.000000   0.000000  ...  135364.444444      0.000000  15548.555556
Tienda en Centro Comercial      0.055838   8.385787   0.010152  ...   32449.263959   5819.593909   3562.022843
Tienda/Salón                    0.011840   1.349727   0.001821  ...   56181.780055   6409.606102   6791.428051

[21 rows x 7 columns]

Promedio de Valor, Condominio e Impuesto por Tipo de inmueble:
                                    Valor    Condominio      Impuesto
Tipo                                                                 
Casa                         31453.177064    909.582569   3259.964220
Casa Comercial               54735.841584    981.074257   4334.559406
Casa de Condominio           51428.609836   4783.920492  11396.206557
Casa de Vecindad              5961.740506    164.854430    313.161392
Cochera/Estacionamiento       6995.454545    277.681818    140.090909
Cocineta                      4425.856061   1427.411846    185.201102
Conjunto Comercial/Sala      57642.614504  16605.811301   3819.485126
Departamento                 18679.804389   6570.124187   1957.273063
Departamento en Hotel        16285.430769   6613.230769   1481.230769
Edificio Completo           409418.080645  24834.129032  27646.241935
Estudio                       8400.000000    960.750000    529.375000
Galpón/Depósito/Almacén     299984.140138   5547.330450  13710.638408
Hotel                        87500.000000      0.000000  21707.000000
Industria                   420000.000000      0.000000      0.000000
Loft                          9924.526316   3224.789474    723.671053
Loteo/Condominio             92166.666667      0.000000  17097.500000
Posada/Chalé                  5180.000000   1032.500000      0.000000
Rancho                       38014.375000      0.000000   1093.750000
Terreno Estándar            135364.444444      0.000000  15548.555556
Tienda en Centro Comercial   32449.263959   5819.593909   3562.022843
Tienda/Salón                 56181.780055   6409.606102   6791.428051

Promedio de Valor por Colonia y Tipo (primeras filas):
                                          Valor
Colonia   Tipo                                 
Ajusco    Casa de Condominio       26250.000000
          Departamento             17150.000000
          Galpón/Depósito/Almacén  42000.000000
          Tienda/Salón              3325.000000
Arboledas Casa                      3733.333333


Explicación de Gemini: 
---------------------

¡Excelente! Has completado correctamente la agrupación y agregación de datos.

Como puedes ver en la salida:

El objeto GroupBy es solo una representación interna de pandas; la magia ocurre cuando le aplicas una función de agregación.
El resultado de agrupado_por_tipo.mean() te da una tabla donde cada fila es un Tipo de inmueble, y las columnas son los promedios de las características numéricas para ese tipo. Esto es muy útil para comparar, por ejemplo, el promedio de habitaciones, área o valor entre diferentes tipos de propiedades.
Al seleccionar columnas después del groupby pero antes de la agregación (agrupado_por_tipo[['Valor', 'Condominio', 'Impuesto']].mean()), obtienes un resumen más enfocado solo en las estadísticas que te interesan, como el promedio de valor, condominio e impuesto por tipo de inmueble. Aquí puedes notar, por ejemplo, que Edificio Completo e Industria tienen promedios de Valor muy altos, lo cual concuerda con lo que vimos en el .describe() donde los valores máximos eran extremos.
Agrupar por múltiples columnas (['Colonia', 'Tipo']) crea un índice de niveles múltiples en el resultado (promedio_por_colonia_tipo), lo que te permite ver estadísticas para combinaciones específicas (por ejemplo, el valor promedio de un Departamento en la colonia Ajusco).
Has realizado un análisis exploratorio básico muy importante. Ahora sabes cómo resumir tus datos por categorías.

Un paso muy común después de agrupar o simplemente para explorar tus datos es ordenar el DataFrame o los resultados de una agregación basándose en los valores de una o más columnas. Esto te ayuda a ver rápidamente los elementos más altos o más bajos, o a organizar tus datos de una manera lógica.

Pandas tiene un método ideal para esto: .sort_values().
'''