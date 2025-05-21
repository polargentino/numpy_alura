import pandas as pd

# Leer el archivo JSON
dt_data = pd.read_json('inmuebles_disponibles.json')
print("Primeras filas del DataFrame:")
print(dt_data.head())
print("\n")

# Información general del DataFrame
print("Información general del DataFrame:")
dt_data.info()
print("\n")

# 4b- Transformar datos para el tipo datetime
# Convertir la columna 'fecha' al tipo datetime
dt_data['fecha'] = pd.to_datetime(dt_data['fecha'])
print("Información del DataFrame después de convertir 'fecha' a datetime:")
dt_data.info()
print("\n")

# Mostrar una muestra de 10 filas del DataFrame
print("Muestra de 10 filas del DataFrame:")
print(dt_data.sample(10))
print("\n")

# 4c- Manipular columnas de tipo datetime a través de métodos.
# Extraer el año y el mes de la columna 'fecha' y formatearlos como 'YYYY-MM'
fechas_ym = dt_data['fecha'].dt.strftime('%Y-%m')
print("Columna 'fecha' formateada como 'YYYY-MM':")
print(fechas_ym.head())
print("\n")

# Agrupar por año y mes y sumar la columna 'lugar_disponible'
subset = dt_data.groupby(dt_data['fecha'].dt.strftime('%Y-%m'))['lugar_disponible'].sum()
print("Suma de 'lugar_disponible' agrupado por año y mes:")
print(subset)

'''
Primeras filas del DataFrame:
    id       fecha  lugar_disponible precio
0  857  2016-01-04             False   None
1  857  2016-01-05             False   None
2  857  2016-01-06             False   None
3  857  2016-01-07             False   None
4  857  2016-01-08             False   None


Información general del DataFrame:
<class 'pandas.core.frame.DataFrame'>
Index: 365000 entries, 0 to 364999
Data columns (total 4 columns):
 #   Column            Non-Null Count   Dtype 
---  ------            --------------   ----- 
 0   id                365000 non-null  int64 
 1   fecha             365000 non-null  object
 2   lugar_disponible  365000 non-null  bool  
 3   precio            270547 non-null  object
dtypes: bool(1), int64(1), object(2)
memory usage: 11.5+ MB


Información del DataFrame después de convertir 'fecha' a datetime:
<class 'pandas.core.frame.DataFrame'>
Index: 365000 entries, 0 to 364999
Data columns (total 4 columns):
 #   Column            Non-Null Count   Dtype         
---  ------            --------------   -----         
 0   id                365000 non-null  int64         
 1   fecha             365000 non-null  datetime64[ns]
 2   lugar_disponible  365000 non-null  bool          
 3   precio            270547 non-null  object        
dtypes: bool(1), datetime64[ns](1), int64(1), object(1)
memory usage: 11.5+ MB


Muestra de 10 filas del DataFrame:
          id      fecha  lugar_disponible   precio
97110   1872 2016-01-24             False     None
357953    20 2016-09-13              True   $85.00
321959  2867 2016-02-02             False     None
158081  2574 2016-02-09             False     None
222605    68 2016-11-19              True   $99.00
221700   842 2016-05-28             False     None
100429   633 2016-02-27             False     None
314332   573 2016-03-11              True  $165.00
346668  3213 2016-10-13              True   $40.00
147453  1188 2016-12-27             False     None


Columna 'fecha' formateada como 'YYYY-MM':
0    2016-01
1    2016-01
2    2016-01
3    2016-01
4    2016-01
Name: fecha, dtype: object


Suma de 'lugar_disponible' agrupado por año y mes:
fecha
2016-01    16543
2016-02    20128
2016-03    23357
2016-04    22597
2016-05    23842
2016-06    23651
2016-07    22329
2016-08    22529
2016-09    22471
2016-10    23765
2016-11    23352
2016-12    24409
2017-01     1574
Name: lugar_disponible, dtype: int64


¡Perfecto! Vemos la salida de cada paso del código que proporcionaste para el manejo de datos de tipo 
datetime.

Con esto, hemos cubierto todos los puntos que me indicaste inicialmente:

Leer archivos JSON, identificar ajustes, normalizar con json_normalize y comprender la fijación de 
precios inteligente.

Identificar y transformar elementos en listas con explode, transformar texto a número con astype, 
tratar texto con números usando apply y tratar varias columnas con applymap.

Manipular texto, usar regex, transformar texto a listas y tokenización.
Identificar, transformar y manipular datos datetime.

'''