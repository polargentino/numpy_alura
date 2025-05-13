# Importamos pandas (si no lo has hecho ya)
import pandas as pd
import numpy as np # Necesario si manejaste 'inf' a NaN
# Importamos la librería matplotlib.pyplot para crear gráficos
import matplotlib.pyplot as plt

# Cargamos el archivo CSV limpio
nombre_archivo = 'alquiler_limpio.csv'
datos_alquiler_limpio = pd.read_csv(nombre_archivo, sep=';')

# --- Nuevo Paso: Visualización de datos (Diagrama de Dispersión) ---

# Para crear un diagrama de dispersión, podemos usar el método .plot() del DataFrame
# y especificar kind='scatter'.
# x: La columna que irá en el eje horizontal (X).
# y: La columna que irá en el eje vertical (Y).

datos_alquiler_limpio.plot(kind='scatter', x='Area', y='Valor')

# Añadir títulos y etiquetas
plt.title('Relación entre Área y Valor de Alquiler')
plt.xlabel('Área (metros cuadrados)')
plt.ylabel('Valor de Alquiler')

# Mostrar el gráfico.
plt.show()

# Podemos también visualizar la relación entre otras columnas numéricas si queremos.
# Por ejemplo, Habitaciones vs Valor:
# datos_alquiler_limpio.plot(kind='scatter', x='Habitaciones', y='Valor')
# plt.title('Relación entre Número de Habitaciones y Valor de Alquiler')
# plt.xlabel('Habitaciones')
# plt.ylabel('Valor de Alquiler')
# plt.show()

# O Área vs la nueva columna Valor_por_Area:
# datos_alquiler_limpio.plot(kind='scatter', x='Area', y='Valor_por_Area')
# plt.title('Relación entre Área y Valor por Área')
# plt.xlabel('Área')
# plt.ylabel('Valor por Área')
# plt.show()

'''
Explicación de Gemini sobre app_5n.png:
---------------------------------------

¡Excelente! Has generado y compartido el diagrama de dispersión de Área vs Valor de Alquiler.

Este gráfico es sumamente revelador:

La gran concentración de puntos en la esquina inferior izquierda confirma que la mayoría de las propiedades tienen áreas pequeñas y valores de alquiler bajos, lo que ya veíamos en el histograma del valor y en las estadísticas descriptivas (la mediana es mucho menor que la media).
Los puntos dispersos y alejados de este grupo principal son claramente los outliers (valores atípicos) que habíamos detectado. Hay propiedades con áreas muy grandes y valores de alquiler muy altos, y también algunas con áreas relativamente pequeñas pero valores de alquiler extremadamente altos.
Este tipo de visualización es crucial porque te permite ver de un vistazo la relación entre variables y la presencia de valores que se comportan de manera muy diferente al resto del dataset. Estos outliers pueden distorsionar significativamente los resultados de análisis estadísticos o modelos de Machine Learning que asumen distribuciones de datos más "normales" o relaciones lineales simples.

Ahora que hemos identificado visualmente estos outliers, un paso común en el proceso de limpieza de datos es decidir cómo manejarlos. Las estrategias varían dependiendo del contexto y de lo que quieras lograr con tu análisis. Algunas opciones son:

Eliminarlos: Si crees que son errores de registro o representan casos muy extremos que no son relevantes para tu análisis principal (por ejemplo, propiedades comerciales gigantes si solo te interesan los alquileres residenciales).
Transformarlos: Aplicar transformaciones matemáticas (como el logaritmo) para reducir el impacto de los valores extremos.
Imputarlos: Reemplazarlos por un valor menos extremo (similar a cómo manejamos los NaNs, pero con una lógica diferente).
Para seguir nuestro aprendizaje gradual, vamos a practicar una estrategia sencilla: eliminar los outliers basados en un umbral en la columna Valor. Esto es una forma de filtrar el DataFrame, algo que ya sabes hacer.

Una manera de decidir el umbral es observar el gráfico y elegir un punto donde los valores se separan claramente de la mayoría de los datos. Otra forma es basarse en estadísticas como los cuartiles o percentiles. Por ejemplo, podríamos decidir eliminar el 1% o el 5% de los valores más altos.

Vamos a eliminar las filas donde el Valor de alquiler es extremadamente alto. Podríamos establecer un umbral visual (por ejemplo, eliminar valores superiores a 10,000,000) o calcular un percentil alto. Usemos un umbral fijo por ahora para simplificar, basado en la observación del gráfico.
'''