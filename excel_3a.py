import pandas as pd

archivo = 'emisiones_CO2.xlsx'
intervalo = pd.read_excel(archivo, sheet_name='emisiones_C02', usecols='A:D')
print(intervalo)
'''
             País ISO 3166-1 alpha-3   Año         Total
0      Afganistán                AFG  1750  0.000000e+00
1      Afganistán                AFG  1751  0.000000e+00
2      Afganistán                AFG  1752  0.000000e+00
3      Afganistán                AFG  1753  0.000000e+00
4      Afganistán                AFG  1754  0.000000e+00
...           ...                ...   ...           ...
63099      Global                WLD  2017  3.609674e+10
63100      Global                WLD  2018  3.682651e+10
63101      Global                WLD  2019  3.708256e+10
63102      Global                WLD  2020  3.526409e+10
63103      Global                WLD  2021  3.712385e+10

[63104 rows x 4 columns]
'''
intervalo.to_excel('co2_percapita.xlsx', index=False)
print(pd.read_excel('co2_percapita.xlsx'))

'''
             País ISO 3166-1 alpha-3   Año         Total
0      Afganistán                AFG  1750  0.000000e+00
1      Afganistán                AFG  1751  0.000000e+00
2      Afganistán                AFG  1752  0.000000e+00
3      Afganistán                AFG  1753  0.000000e+00
4      Afganistán                AFG  1754  0.000000e+00
...           ...                ...   ...           ...
63099      Global                WLD  2017  3.609674e+10
63100      Global                WLD  2018  3.682651e+10
63101      Global                WLD  2019  3.708256e+10
63102      Global                WLD  2020  3.526409e+10
63103      Global                WLD  2021  3.712385e+10


Explicación de Mistral AI:
--------------------------

Este código utiliza la biblioteca pandas para leer datos de un archivo Excel, manipularlos y luego 
guardarlos en un nuevo archivo Excel. Aquí está la explicación línea por línea:

import pandas as pd: Importa la biblioteca pandas y la alias como pd. Pandas es una biblioteca de 
Python utilizada para la manipulación y análisis de datos.

archivo = 'emisiones_CO2.xlsx': Asigna el nombre del archivo Excel a una variable llamada archivo.
intervalo = pd.read_excel(archivo, sheet_name='emisiones_C02', usecols='A:D'): Utiliza la función 
read_excel de pandas para leer el archivo Excel y cargar los datos en un DataFrame llamado intervalo.
sheet_name='emisiones_C02': Especifica el nombre de la hoja que deseas leer.
usecols='A:D': Indica que deseas leer solo las columnas desde la A hasta la D.

print(intervalo): Imprime el DataFrame intervalo, mostrando los datos contenidos en el archivo Excel. 
La salida muestra un DataFrame con las columnas "País", "ISO 3166-1 alpha-3", "Año" y "Total", y 
todas las filas de datos.

intervalo.to_excel('co2_percapita.xlsx', index=False): Guarda el DataFrame intervalo en un nuevo 
archivo Excel llamado co2_percapita.xlsx.
index=False: Indica que no se debe guardar el índice del DataFrame en el archivo Excel.

print(pd.read_excel('co2_percapita.xlsx')): Lee el nuevo archivo Excel co2_percapita.xlsx y lo 
imprime, mostrando los datos contenidos en el archivo. La salida es similar a la del DataFrame 
original, confirmando que los datos se han guardado correctamente


Resumen
Este código realiza las siguientes acciones:

Lee un archivo Excel y carga los datos en un DataFrame.
Imprime el DataFrame para mostrar los datos.
Guarda el DataFrame en un nuevo archivo Excel.
Lee e imprime el nuevo archivo Excel para verificar que los datos se han guardado correctamente.
Este flujo de trabajo es útil para manipular y guardar datos de manera eficiente utilizando pandas.

'''