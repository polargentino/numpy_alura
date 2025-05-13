# Importamos pandas (si no lo has hecho ya)
import pandas as pd
import numpy as np # Necesario si manejaste 'inf' a NaN
# Importamos la librería matplotlib.pyplot para crear gráficos
import matplotlib.pyplot as plt

# Cargamos el archivo CSV (podemos cargar el original o el limpio que acabas de guardar)
# Vamos a usar el DataFrame limpio para visualizar los datos ya tratados.
nombre_archivo = 'alquiler_limpio.csv' # Usamos el archivo limpio que guardamos
# Asegúrate de usar el separador correcto al leer el archivo limpio
datos_alquiler_limpio = pd.read_csv(nombre_archivo, sep=';')


# --- Nuevo Paso: Visualización de datos (Histograma) ---

# Seleccionamos la columna numérica que queremos visualizar, por ejemplo 'Valor'.
# Podemos usar el método .hist() directamente en la Serie de pandas.
# .hist() es un método conveniente proporcionado por pandas que utiliza matplotlib por debajo.
# bins: Define cuántas "barras" o rangos quieres en tu histograma. Más barras dan más detalle.
datos_alquiler_limpio['Valor'].hist(bins=50) # Experimenta con diferentes números de bins

# Añadir títulos y etiquetas para que el gráfico sea comprensible.
plt.title('Distribución de Valores de Alquiler')
plt.xlabel('Valor de Alquiler')
plt.ylabel('Frecuencia')

# Mostrar el gráfico. Este comando es necesario para que la ventana del gráfico aparezca.
plt.show()

# También podemos crear un histograma para otra columna numérica, por ejemplo 'Area'.
# datos_alquiler_limpio['Area'].hist(bins=50)
# plt.title('Distribución de Área')
# plt.xlabel('Área')
# plt.ylabel('Frecuencia')
# plt.show()

# O incluso para la nueva columna 'Valor_por_Area' (recuerda que puede tener NaNs si no los rellenaste)
# datos_alquiler_limpio['Valor_por_Area'].hist(bins=50)
# plt.title('Distribución de Valor por Área')
# plt.xlabel('Valor por Área')
# plt.ylabel('Frecuencia')
# plt.show()

'''
¡Excelente! Has generado y compartido el histograma de la columna Valor.

Este gráfico es una visualización muy poderosa de lo que ya habíamos intuido con las estadísticas 
descriptivas (.describe()):

La barra altísima cerca del 0 en el eje horizontal ("Valor de Alquiler") nos confirma visualmente que 
la gran mayoría de los valores de alquiler son bajos.

El eje horizontal se extiende hasta valores muy altos (5e7, que es 50,000,000), pero casi no hay 
barras en ese rango. Esto demuestra claramente la presencia de valores atípicos (outliers) 
extremadamente altos que "estiran" el eje y hacen que la distribución parezca tan sesgada. Estos son 
los valores que vimos en el .describe() con un max muy elevado y que hicieron que la mean fuera mucho
 mayor que la median.

Este histograma confirma la necesidad de ser conscientes de estos valores extremos al analizar la 
columna Valor.

Ahora que hemos visualizado la distribución de una sola variable numérica, un paso muy común en la 
exploración es visualizar la relación entre dos variables numéricas. Esto puede ayudarnos a ver si 
hay alguna correlación o patrón entre ellas.

Dado que acabamos de crear la columna Valor_por_Area, sería interesante ver la relación entre Area y 
Valor. Un diagrama de dispersión (scatter plot) es ideal para esto. Cada punto en el gráfico 
representará una propiedad, con su área en un eje y su valor en el otro.

Vamos a crear un diagrama de dispersión de Area vs Valor. app_5m.png
'''