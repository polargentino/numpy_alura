# Importamos pandas (si no lo has hecho ya)
import pandas as pd
import numpy as np # Necesario si manejaste 'inf' a NaN

# Cargamos el archivo CSV (si no lo has hecho ya)
nombre_archivo = 'alquiler.csv'
datos_alquiler = pd.read_csv(nombre_archivo, sep=';')

# --- Manejo de valores faltantes y creación de nuevas columnas (usamos el mismo código de antes) ---
datos_alquiler_limpio = datos_alquiler.copy()
datos_alquiler_limpio['Condominio'] = datos_alquiler_limpio['Condominio'].fillna(0)
datos_alquiler_limpio['Impuesto'] = datos_alquiler_limpio['Impuesto'].fillna(0)
mediana_valor_final = datos_alquiler_limpio['Valor'].median()
datos_alquiler_limpio['Valor'] = datos_alquiler_limpio['Valor'].fillna(mediana_valor_final)

# Creamos 'Valor_por_Area' y manejamos 'inf'
datos_alquiler_limpio['Valor_por_Area'] = datos_alquiler_limpio['Valor'] / datos_alquiler_limpio['Area']
datos_alquiler_limpio['Valor_por_Area'] = datos_alquiler_limpio['Valor_por_Area'].replace([np.inf, -np.inf], np.nan)
# Opcional: rellenar los NaNs resultantes en 'Valor_por_Area'
# mediana_valor_por_area = datos_alquiler_limpio['Valor_por_Area'].median()
# datos_alquiler_limpio['Valor_por_Area'] = datos_alquiler_limpio['Valor_por_Area'].fillna(mediana_valor_por_area)
# Si no rellenas, los NaNs quedarán en el archivo guardado.

# Creamos 'Es_Grande'
datos_alquiler_limpio['Es_Grande'] = datos_alquiler_limpio['Area'] > 200


# --- Nuevo Paso: Guardar el DataFrame en un archivo CSV ---

# Definimos el nombre del nuevo archivo CSV.
nombre_archivo_salida = 'alquiler_limpio.csv'

# Usamos el método .to_csv() en el DataFrame que queremos guardar.
# El primer argumento es el nombre del archivo de salida.
# 'index=False' es muy importante: le dice a pandas que NO escriba el índice del DataFrame
# como una columna en el archivo CSV. Si no pones esto, tendrás una columna extra con los números del índice.
# 'sep=';'' especifica que queremos usar el punto y coma como separador en el nuevo archivo,
# al igual que el archivo original. Puedes cambiarlo a ',' si prefieres CSV estándar.
datos_alquiler_limpio.to_csv(nombre_archivo_salida, index=False, sep=';')

print(f"\nDataFrame guardado exitosamente en '{nombre_archivo_salida}'")

# Para verificar, podrías incluso leer este nuevo archivo:
# datos_guardados = pd.read_csv(nombre_archivo_salida, sep=';')
# print("\nPrimeras filas del archivo guardado:")
# print(datos_guardados.head())

'''
DataFrame guardado exitosamente en 'alquiler_limpio.csv'


Explicación de Gemini: 
---------------------

¡Excelente! Has guardado tu DataFrame limpio y transformado en un nuevo archivo CSV 
(alquiler_limpio.csv). El output que muestras es el contenido de las primeras filas de este nuevo 
archivo, confirmando que las columnas Valor_por_Area y Es_Grande fueron añadidas correctamente y 
que los valores faltantes en Condominio e Impuesto (y probablemente en Valor y Valor_por_Area si 
tenías NaNs allí) fueron rellenados con 0.0 o la mediana según tu código.

¡Has completado un ciclo fundamental en el manejo de datos con pandas! Desde la carga inicial, 
pasando por la exploración, limpieza, transformación (creación de nuevas columnas), hasta guardar el
resultado.

Ahora que tienes tus datos preparados, el siguiente paso lógico en la mayoría de los flujos de 
trabajo de análisis de datos es la visualización. Ver tus datos en gráficos te puede revelar 
patrones, tendencias y valores atípicos de una manera mucho más intuitiva y rápida que las tablas y
estadísticas numéricas.

Para visualizar datos en Python, comúnmente usamos librerías como Matplotlib o Seaborn. Pandas 
tiene una excelente integración con Matplotlib, permitiéndonos crear gráficos directamente desde 
DataFrames y Series.

Vamos a empezar con una visualización muy básica pero informativa: un histograma de la columna Valor.
Un histograma muestra la distribución de una variable numérica, es decir, cuántas veces los valores 
caen dentro de diferentes "contenedores" o rangos. Esto nos ayudará a visualizar la distribución de 
los precios de alquiler y a confirmar visualmente si hay muchos valores altos que sesgan los datos, 
como sugerían las estadísticas descriptivas.

Aquí tienes el código para crear el histograma, con comentarios. Necesitarás tener instalada la 
librería matplotlib (pip install matplotlib).



Tipo;Colonia;Habitaciones;Garages;Suites;Area;Valor;Condominio;Impuesto;Valor_por_Area;Es_Grande
Cocineta;Condesa;1;0;0;40;5950.0;1750.0;210.0;148.75;False
Casa;Polanco;2;0;1;100;24500.0;0.0;0.0;245.0;False
Conjunto Comercial/Sala;Santa Fe;0;4;0;150;18200.0;14070.0;3888.5;121.33333333333333;False
Departamento;Centro Histórico;1;0;0;15;2800.0;1365.0;70.0;186.66666666666666;False
Departamento;Del Valle;1;0;0;48;2800.0;805.0;0.0;58.333333333333336;False
'''