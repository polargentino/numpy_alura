'''
Por Mistral AI: 
--------------

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

Normalizar la columna nutritions:

df_normalizado = pd.concat([df.drop(['nutritions'], axis=1), df['nutritions'].apply(pd.Series)], 
axis=1): Expande el diccionario nutritions en columnas separadas y combina las columnas originales 
con las nuevas columnas.

Imprimir el DataFrame normalizado:

print(df_normalizado.head()): Imprime las primeras filas del DataFrame normalizado.
Este código te permitirá expandir la columna nutritions en columnas separadas, facilitando el 
análisis y la manipulación de los datos. Si tienes más preguntas o necesitas más ayuda, no dudes 
en decírmelo.
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

# Normalizar la columna 'nutritions'
df_normalizado = pd.concat([
    df.drop(['nutritions'], axis=1),
    df['nutritions'].apply(pd.Series)
], axis=1)

# Imprimir el DataFrame normalizado
print("\nDataFrame normalizado:")
print(df_normalizado.head())

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

DataFrame normalizado:
         name  id      family         order      genus  calories  fat  sugar  carbohydrates  protein
0   Persimmon  52   Ebenaceae       Rosales  Diospyros      81.0  0.0   18.0           18.0      0.0
1  Strawberry   3    Rosaceae       Rosales   Fragaria      29.0  0.4    5.4            5.5      0.8
2      Banana   1    Musaceae  Zingiberales       Musa      96.0  0.2   17.2           22.0      1.0
3      Tomato   5  Solanaceae     Solanales    Solanum      74.0  0.2    2.6            3.9      0.9
4        Pear   4    Rosaceae       Rosales      Pyrus      57.0  0.1   10.0           15.0      0.4




¡Excelente! Has logrado normalizar el DataFrame y expandir la columna nutritions en columnas 
separadas. Ahora tienes un DataFrame con columnas individuales para cada valor nutricional, lo que 
facilita el análisis y la manipulación de los datos.

Resumen del DataFrame Normalizado
El DataFrame normalizado tiene las siguientes columnas:

name: Nombre de la fruta.
id: Identificador único de la fruta.
family: Familia de la fruta.
order: Orden de la fruta.
genus: Género de la fruta.
calories: Calorías de la fruta.
fat: Grasa de la fruta.
sugar: Azúcar de la fruta.
carbohydrates: Carbohidratos de la fruta.
protein: Proteína de la fruta.
Ejemplo de Análisis de Datos
Con el DataFrame normalizado, puedes realizar varios tipos de análisis. Aquí tienes algunos ejemplos:

Filtrar Frutas con Alto Contenido de Azúcar:

Puedes filtrar las frutas que tienen un alto contenido de azúcar para identificar qué frutas son más 
dulces.

Copiar

frutas_altas_en_azucar = df_normalizado[df_normalizado['sugar'] > 10]
print(frutas_altas_en_azucar)

Calcular el Promedio de Calorías:

Puedes calcular el promedio de calorías de todas las frutas.
Copiar

promedio_calorias = df_normalizado['calories'].mean()
print(f"Promedio de calorías: {promedio_calorias}")

Visualizar los Datos:

Puedes usar bibliotecas como matplotlib o seaborn para visualizar los datos. Por ejemplo, para crear 
un gráfico de barras de las calorías de las frutas:
Copiar

import matplotlib.pyplot as plt

plt.bar(df_normalizado['name'], df_normalizado['calories'])
plt.xlabel('Fruta')
plt.ylabel('Calorías')
plt.title('Calorías por Fruta')
plt.xticks(rotation=90)
plt.show()

Conclusión
Con el DataFrame normalizado, tienes una base sólida para realizar análisis detallados y obtener 
insights valiosos sobre los datos nutricionales de las frutas. Si tienes más preguntas o necesitas 
más ayuda, no dudes en decírmelo.
'''