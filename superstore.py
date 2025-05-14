import pandas as pd
import chardet

with open('superstore_data.csv', 'rb') as file:
    print(chardet.detect(file.read()))

datos = pd.read_csv('superstore_data.csv')
print(datos.head())

'''
{'encoding': 'ascii', 'confidence': 1.0, 'language': ''}

      Id  Year_Birth   Education Marital_Status  ...  NumStorePurchases  NumWebVisitsMonth  Response Complain
0   1826        1970  Graduation       Divorced  ...                  6                  1         1        0
1      1        1961  Graduation         Single  ...                  7                  5         1        0
2  10476        1958  Graduation        Married  ...                  5                  2         0        0
3   1386        1967  Graduation       Together  ...                  2                  7         0        0
4   5371        1989  Graduation         Single  ...                  2                  7         1        0

[5 rows x 22 columns]


Explicación de Mistral AI:
-------------------------

Explicación:
Importación de Bibliotecas:

pandas: Se utiliza para la manipulación y análisis de datos. Aquí se usa para leer el archivo CSV y 
cargarlo en un DataFrame.

chardet: Se utiliza para detectar la codificación de caracteres del archivo CSV.
Detección de Codificación:

Se abre el archivo en modo binario y se lee su contenido para detectar la codificación utilizando 
chardet.detect().

El resultado de la detección se imprime, mostrando la codificación detectada, la confianza en la 
detección y el lenguaje.

Lectura del Archivo CSV:

Se utiliza pd.read_csv() para leer el archivo CSV y cargar los datos en un DataFrame de pandas.
Vista Previa de los Datos:

Se imprime una vista previa de los datos utilizando datos.head(), que muestra las primeras 5 filas 
del DataFrame.

Resultado:

Se muestra el resultado de la detección de codificación y una vista previa de los datos, incluyendo 
las columnas y las primeras filas del DataFrame.

Este código es útil para cargar y explorar inicialmente un conjunto de datos almacenado en un archivo 
CSV.
'''