import pandas as pd
import numpy as np

# Cargar el conjunto de datos
df_data = pd.read_json('inmuebles_disponibles.json')

# Mostrar las primeras filas para verificar la carga (opcional)
print("DataFrame original:")
print(df_data.head())
print("\nInformación del DataFrame original:")
print(df_data.info())

# 1. Llenar los valores vacíos en la columna 'precio' con '0.0'
# El parámetro inplace=True modifica el DataFrame directamente.
# df_data['precio'].fillna('0.0', inplace=True) - ADVERTENCIA - Cambiar por : abajo
df_data['precio'] = df_data['precio'].fillna('0.0')
# 2. Eliminar el símbolo '$' y las comas ',' de la columna 'precio'
# Usamos apply con una función lambda para realizar el reemplazo en cada valor.
df_data['precio'] = df_data['precio'].apply(lambda x: x.replace('$', '').replace(',', ''))

# 3. Transformar el tipo de datos de la columna 'precio' a float64
df_data['precio'] = df_data['precio'].astype(np.float64)

# Observar el resultado final
print("\nDataFrame después de la transformación de 'precio':")
print(df_data.head())
print("\nInformación del DataFrame después de la transformación:")
print(df_data.info())

# Verificar los tipos de datos y algunos valores de la columna 'precio'
print("\nPrimeros valores de la columna 'precio' transformada:")
print(df_data['precio'].head())
print(f"\nTipo de dato de la columna 'precio': {df_data['precio'].dtype}")

'''
DataFrame original:
    id       fecha  lugar_disponible precio
0  857  2016-01-04             False   None
1  857  2016-01-05             False   None
2  857  2016-01-06             False   None
3  857  2016-01-07             False   None
4  857  2016-01-08             False   None

Información del DataFrame original:
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
None

DataFrame después de la transformación de 'precio':
    id       fecha  lugar_disponible  precio
0  857  2016-01-04             False     0.0
1  857  2016-01-05             False     0.0
2  857  2016-01-06             False     0.0
3  857  2016-01-07             False     0.0
4  857  2016-01-08             False     0.0

Información del DataFrame después de la transformación:
<class 'pandas.core.frame.DataFrame'>
Index: 365000 entries, 0 to 364999
Data columns (total 4 columns):
 #   Column            Non-Null Count   Dtype  
---  ------            --------------   -----  
 0   id                365000 non-null  int64  
 1   fecha             365000 non-null  object 
 2   lugar_disponible  365000 non-null  bool   
 3   precio            365000 non-null  float64
dtypes: bool(1), float64(1), int64(1), object(1)
memory usage: 11.5+ MB
None

Primeros valores de la columna 'precio' transformada:
0    0.0
1    0.0
2    0.0
3    0.0
4    0.0
Name: precio, dtype: float64

Tipo de dato de la columna 'precio': float64




Explicación del Código:
Importar librerías:

pandas se importa como pd para la manipulación de DataFrames.
numpy se importa como np para utilizar np.float64 al convertir el tipo de dato.
Cargar datos:

pd.read_json('inmuebles_disponibles.json') carga tus datos en un DataFrame llamado df_data.
Tratamiento de la columna precio:

df_data['precio'].fillna('0.0', inplace=True): Esta línea busca todos los valores nulos (NaN) en la columna precio y los reemplaza por la cadena de texto '0.0'. El argumento inplace=True asegura que la modificación se haga directamente sobre df_data sin necesidad de reasignarlo.
df_data['precio'] = df_data['precio'].apply(lambda x: x.replace('$', '').replace(',', '')): Aquí se aplica una función a cada elemento de la columna precio.
apply(lambda x: ...): Permite aplicar una función personalizada.
lambda x: x.replace('$', '').replace(',', ''): Es una función anónima que toma un valor x (cada precio como string) y le quita el símbolo $ y las comas ,.
df_data['precio'] = df_data['precio'].astype(np.float64): Finalmente, esta línea convierte todos los valores de la columna precio (que ahora son strings de números, por ejemplo, '1500.50' o '0.0') al tipo numérico float64.
Verificación:

Las sentencias print() te permiten ver las primeras filas (head()) y la información general del DataFrame (info()) antes y después de las transformaciones para confirmar que los cambios se aplicaron correctamente, especialmente el tipo de dato de la columna precio.
'''