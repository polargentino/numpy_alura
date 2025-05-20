import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leer el archivo JSON
datos = pd.read_json('dados_vendas_clientes.json')

# Mostrar las primeras filas del DataFrame
print("Primeras filas del DataFrame original:")
print(datos.head())

# Normalizar la columna 'dados_vendas'
datos = pd.json_normalize(datos['dados_vendas'])

# Mostrar las primeras filas del DataFrame normalizado
print("\nPrimeras filas del DataFrame normalizado:")
print(datos.head())

# Colectar los valores de las columnas y verificar
columnas = list(datos.columns)
print("\nColumnas del DataFrame:")
print(columnas)

# Destrincar las listas con explode
datos = datos.explode('Valor da compra')

# Resetear los índices de las líneas
datos.reset_index(drop=True, inplace=True)

# Observar el DataFrame después de explode
print("\nPrimeras filas del DataFrame después de explode:")
print(datos.head())

# Verificar los tipos de datos con info
print("\nInformación del DataFrame:")
print(datos.info())

# La columna numérica es 'Valor da compra'
print("\nColumna 'Valor da compra':")
print(datos['Valor da compra'])

# Iniciar la transformación
# Remover los textos presentes en la base
# Cambiar las comas separadoras del decimal por punto
datos['Valor da compra'] = datos['Valor da compra'].apply(lambda x: x.replace('R$ ', '').replace(',', '.').strip())

# Cambiar el tipo de datos para float
datos['Valor da compra'] = datos['Valor da compra'].astype(np.float64)

# Verificar la transformación
print("\nInformación del DataFrame después de la transformación:")
print(datos.info())

# Mostrar las primeras filas del DataFrame después de la transformación
print("\nPrimeras filas del DataFrame después de la transformación:")
print(datos.head())

# Convertir la columna 'Cliente' a una lista de clientes únicos
datos['Cliente'] = datos['Cliente'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)

print("\nPrimeras filas del DataFrame después de convertir 'Cliente':")
print(datos.head())

# Calcular estadísticas descriptivas para las columnas numéricas
print("\nEstadísticas descriptivas para las columnas numéricas:")
print(datos['Valor da compra'].describe())

# Crear un histograma de los valores de compra
plt.hist(datos['Valor da compra'].dropna(), bins=20)
plt.xlabel('Valor da compra')
plt.ylabel('Frecuencia')
plt.title('Distribución de Valores de Compra')
plt.show()

'''
Primeras filas del DataFrame original:
                                        dados_vendas
0  {'Data de venda': '06/06/2022', 'Cliente': ['@...
1  {'Data de venda': '07/06/2022', 'Cliente': ['I...
2  {'Data de venda': '08/06/2022', 'Cliente': ['I...
3  {'Data de venda': '09/06/2022', 'Cliente': ['J...
4  {'Data de venda': '10/06/2022', 'Cliente': ['M...

Primeras filas del DataFrame normalizado:
  Data de venda  ...                               Valor da compra
0    06/06/2022  ...    [R$ 836,5, R$ 573,33, R$ 392,8, R$ 512,34]
1    07/06/2022  ...  [R$ 825,31, R$ 168,07, R$ 339,18, R$ 314,69]
2    08/06/2022  ...  [R$ 682,05, R$ 386,34, R$ 622,65, R$ 630,79]
3    09/06/2022  ...   [R$ 390,3, R$ 759,16, R$ 334,47, R$ 678,78]
4    10/06/2022  ...  [R$ 314,24, R$ 311,15, R$ 899,16, R$ 885,24]

[5 rows x 3 columns]

Columnas del DataFrame:
['Data de venda', 'Cliente', 'Valor da compra']

Primeras filas del DataFrame después de explode:
  Data de venda                                            Cliente Valor da compra
0    06/06/2022  [@ANA _LUCIA 321, DieGO ARMANDIU 210, DieGO AR...        R$ 836,5
1    06/06/2022  [@ANA _LUCIA 321, DieGO ARMANDIU 210, DieGO AR...       R$ 573,33
2    06/06/2022  [@ANA _LUCIA 321, DieGO ARMANDIU 210, DieGO AR...        R$ 392,8
3    06/06/2022  [@ANA _LUCIA 321, DieGO ARMANDIU 210, DieGO AR...       R$ 512,34
4    07/06/2022  [Isabely JOanes 738, Isabely JOanes 738, Isabe...       R$ 825,31

Información del DataFrame:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20 entries, 0 to 19
Data columns (total 3 columns):
 #   Column           Non-Null Count  Dtype 
---  ------           --------------  ----- 
 0   Data de venda    20 non-null     object
 1   Cliente          20 non-null     object
 2   Valor da compra  20 non-null     object
dtypes: object(3)
memory usage: 608.0+ bytes
None

Columna 'Valor da compra':
0      R$ 836,5
1     R$ 573,33
2      R$ 392,8
3     R$ 512,34
4     R$ 825,31
5     R$ 168,07
6     R$ 339,18
7     R$ 314,69
8     R$ 682,05
9     R$ 386,34
10    R$ 622,65
11    R$ 630,79
12     R$ 390,3
13    R$ 759,16
14    R$ 334,47
15    R$ 678,78
16    R$ 314,24
17    R$ 311,15
18    R$ 899,16
19    R$ 885,24
Name: Valor da compra, dtype: object

Información del DataFrame después de la transformación:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20 entries, 0 to 19
Data columns (total 3 columns):
 #   Column           Non-Null Count  Dtype  
---  ------           --------------  -----  
 0   Data de venda    20 non-null     object 
 1   Cliente          20 non-null     object 
 2   Valor da compra  20 non-null     float64
dtypes: float64(1), object(2)
memory usage: 608.0+ bytes
None

Primeras filas del DataFrame después de la transformación:
  Data de venda                                            Cliente  Valor da compra
0    06/06/2022  [@ANA _LUCIA 321, DieGO ARMANDIU 210, DieGO AR...           836.50
1    06/06/2022  [@ANA _LUCIA 321, DieGO ARMANDIU 210, DieGO AR...           573.33
2    06/06/2022  [@ANA _LUCIA 321, DieGO ARMANDIU 210, DieGO AR...           392.80
3    06/06/2022  [@ANA _LUCIA 321, DieGO ARMANDIU 210, DieGO AR...           512.34
4    07/06/2022  [Isabely JOanes 738, Isabely JOanes 738, Isabe...           825.31

Primeras filas del DataFrame después de convertir 'Cliente':
  Data de venda                                            Cliente  Valor da compra
0    06/06/2022  @ANA _LUCIA 321, DieGO ARMANDIU 210, DieGO ARM...           836.50
1    06/06/2022  @ANA _LUCIA 321, DieGO ARMANDIU 210, DieGO ARM...           573.33
2    06/06/2022  @ANA _LUCIA 321, DieGO ARMANDIU 210, DieGO ARM...           392.80
3    06/06/2022  @ANA _LUCIA 321, DieGO ARMANDIU 210, DieGO ARM...           512.34
4    07/06/2022  Isabely JOanes 738, Isabely JOanes 738, Isabel...           825.31

Estadísticas descriptivas para las columnas numéricas:
count     20.000000
mean     542.827500
std      225.301753
min      168.070000
25%      338.002500
50%      542.835000
75%      701.327500
max      899.160000
Name: Valor da compra, dtype: float64



Explicación del Código:
Normalizar la columna dados_vendas:

datos = pd.json_normalize(datos['dados_vendas']): Normaliza la columna dados_vendas para convertirla en un DataFrame.
Destrincar las listas con explode:

datos = datos.explode('Valor da compra'): Expande la columna Valor da compra para que cada elemento de la lista tenga su propia fila.
Resetear los índices de las líneas:

datos.reset_index(drop=True, inplace=True): Resetea el índice del DataFrame para que sea secuencial.
Transformar la columna numérica a tipo numérico:

datos['Valor da compra'] = datos['Valor da compra'].apply(lambda x: x.replace('R$ ', '').replace(',', '.').strip()): Limpia la columna Valor da compra eliminando el símbolo R$ y cambiando las comas por puntos.
datos['Valor da compra'] = datos['Valor da compra'].astype(np.float64): Convierte la columna Valor da compra a tipo float64.

Pasos Adicionales para Análisis de Datos
Aquí tienes algunas sugerencias para continuar con el análisis de los datos:

Convertir la columna Cliente a un formato más manejable:

Puedes convertir la columna Cliente a un formato más manejable, como una lista de clientes únicos.
'''



