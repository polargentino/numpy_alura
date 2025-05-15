'''
Explicación del Código:
Obtener los datos de la API:

datos_frutas = requests.get('https://fruityvice.com/api/fruit/all'): Realiza una solicitud GET a la 
API de Fruitvice para obtener datos de todas las frutas.

Convertir la respuesta a JSON:

resultado = json.loads(datos_frutas.text): Convierte el texto de la respuesta en un objeto JSON.
Convertir el JSON a un DataFrame de pandas:

df = pd.DataFrame(resultado): Convierte el objeto JSON en un DataFrame de pandas.
Proporcionar las primeras filas del DataFrame:

print(df.head()): Imprime las primeras filas del DataFrame.
Proporcionar los nombres de las columnas:

print(df.columns): Imprime los nombres de las columnas del DataFrame.
Proporcionar información sobre los tipos de datos y valores no nulos:

print(df.info()): Imprime información sobre los tipos de datos y la cantidad de valores no nulos en 
cada columna.

Manejar errores:

try-except: Intenta acceder a una columna que no existe para mostrar cómo manejar errores.
Este código te proporcionará una visión básica de los datos obtenidos de la API de Fruitvice y te 
ayudará a entender la estructura del DataFrame. Si tienes más preguntas o necesitas más ayuda, no 
dudes en decírmelo
'''

import pandas as pd
import requests
import json

# Obtener los datos de la API Fruitvice
datos_frutas = requests.get('https://fruityvice.com/api/fruit/all')

# Convertir la respuesta a JSON
resultado = json.loads(datos_frutas.text)

# Convertir el JSON a un DataFrame de pandas
df = pd.DataFrame(resultado)

# Proporciona las primeras filas del DataFrame
print("Primeras filas del DataFrame:")
print(df.head())

# Proporciona los nombres de las columnas
print("\nNombres de las columnas:")
print(df.columns)

# Proporciona información sobre los tipos de datos y valores no nulos
print("\nInformación del DataFrame:")
print(df.info())

# Si hay un error, proporciona el mensaje de error completo
try:
    # Código que causa el error
    # Por ejemplo, intentar acceder a una columna que no existe
    resultado = df['columna_inexistente']
except Exception as e:
    print(f"\nError: {e}")

'''
Primeras filas del DataFrame:
         name  id      family         order      genus                                         nutritions
0   Persimmon  52   Ebenaceae       Rosales  Diospyros  {'calories': 81, 'fat': 0.0, 'sugar': 18.0, 'c...
1  Strawberry   3    Rosaceae       Rosales   Fragaria  {'calories': 29, 'fat': 0.4, 'sugar': 5.4, 'ca...
2      Banana   1    Musaceae  Zingiberales       Musa  {'calories': 96, 'fat': 0.2, 'sugar': 17.2, 'c...
3      Tomato   5  Solanaceae     Solanales    Solanum  {'calories': 74, 'fat': 0.2, 'sugar': 2.6, 'ca...
4        Pear   4    Rosaceae       Rosales      Pyrus  {'calories': 57, 'fat': 0.1, 'sugar': 10.0, 'c...

Nombres de las columnas:
Index(['name', 'id', 'family', 'order', 'genus', 'nutritions'], dtype='object')

Información del DataFrame:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 49 entries, 0 to 48
Data columns (total 6 columns):
 #   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   name        49 non-null     object
 1   id          49 non-null     int64 
 2   family      49 non-null     object
 3   order       49 non-null     object
 4   genus       49 non-null     object
 5   nutritions  49 non-null     object
dtypes: int64(1), object(5)
memory usage: 2.4+ KB
None

Error: 'columna_inexistente'
'''
