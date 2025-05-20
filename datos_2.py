import pandas as pd
import numpy as np

# Leer el archivo JSON
datos = pd.read_json('dados_locacao_imoveis.json')

# Mostrar las primeras filas del DataFrame
print("Primeras filas del DataFrame original:")
print(datos.head())

# Normalizar la columna 'dados_locacao'
datos = pd.json_normalize(datos['dados_locacao'])

# Mostrar las primeras filas del DataFrame normalizado
print("\nPrimeras filas del DataFrame normalizado:")
print(datos.head())

# Colectar los valores de las columnas y verificar
columnas = list(datos.columns)
print("\nColumnas del DataFrame:")
print(columnas)

# Destrincar las listas con explode
# Asegúrate de que las columnas que contienen listas sean las correctas
# Aquí, asumimos que 'valor_aluguel' es una columna que contiene listas
if 'valor_aluguel' in columnas:
    datos = datos.explode('valor_aluguel')

# Resetear los índices de las líneas
datos.reset_index(drop=True, inplace=True)

# Observar el DataFrame después de explode
print("\nPrimeras filas del DataFrame después de explode:")
print(datos.head())

# Verificar los tipos de datos con info
print("\nInformación del DataFrame:")
print(datos.info())

# La columna numérica es 'valor_aluguel'
if 'valor_aluguel' in columnas:
    print("\nColumna 'valor_aluguel':")
    print(datos['valor_aluguel'])

    # Iniciar la transformación
    # Remover los textos presentes en la base
    # Cambiar las comas separadoras del decimal por punto
    datos['valor_aluguel'] = datos['valor_aluguel'].apply(lambda x: x.replace('$ ', '').replace(' reais', '').replace(',', '.').strip())

    # Cambiar el tipo de datos para float
    datos['valor_aluguel'] = datos['valor_aluguel'].astype(np.float64)

    # Verificar la transformación
    print("\nInformación del DataFrame después de la transformación:")
    print(datos.info())

    # Mostrar las primeras filas del DataFrame después de la transformación
    print("\nPrimeras filas del DataFrame después de la transformación:")
    print(datos.head())
else:
    print("\nLa columna 'valor_aluguel' no está presente en el DataFrame.")

'''
Primeras filas del DataFrame original:
                                       dados_locacao
0  {'apartamento': 'A101 (blocoAP)', 'datas_combi...
1  {'apartamento': 'A102 (blocoAP)', 'datas_combi...
2  {'apartamento': 'B201 (blocoAP)', 'datas_combi...
3  {'apartamento': 'B202 (blocoAP)', 'datas_combi...
4  {'apartamento': 'C301 (blocoAP)', 'datas_combi...

Primeras filas del DataFrame normalizado:
      apartamento datas_combinadas_pagamento        datas_de_pagamento                     valor_aluguel
0  A101 (blocoAP)   [01/06/2022, 01/07/2022]  [05/06/2022, 03/07/2022]  [$ 1000,0 reais, $ 2500,0 reais]
1  A102 (blocoAP)   [02/06/2022, 02/07/2022]  [02/06/2022, 06/07/2022]  [$ 1100,0 reais, $ 2600,0 reais]
2  B201 (blocoAP)   [03/06/2022, 03/07/2022]  [07/06/2022, 03/07/2022]  [$ 1200,0 reais, $ 2700,0 reais]
3  B202 (blocoAP)   [04/06/2022, 04/07/2022]  [07/06/2022, 05/07/2022]  [$ 1300,0 reais, $ 2800,0 reais]
4  C301 (blocoAP)   [05/06/2022, 05/07/2022]  [10/06/2022, 09/07/2022]  [$ 1400,0 reais, $ 2900,0 reais]

Columnas del DataFrame:
['apartamento', 'datas_combinadas_pagamento', 'datas_de_pagamento', 'valor_aluguel']

Primeras filas del DataFrame después de explode:
      apartamento datas_combinadas_pagamento        datas_de_pagamento   valor_aluguel
0  A101 (blocoAP)   [01/06/2022, 01/07/2022]  [05/06/2022, 03/07/2022]  $ 1000,0 reais
1  A101 (blocoAP)   [01/06/2022, 01/07/2022]  [05/06/2022, 03/07/2022]  $ 2500,0 reais
2  A102 (blocoAP)   [02/06/2022, 02/07/2022]  [02/06/2022, 06/07/2022]  $ 1100,0 reais
3  A102 (blocoAP)   [02/06/2022, 02/07/2022]  [02/06/2022, 06/07/2022]  $ 2600,0 reais
4  B201 (blocoAP)   [03/06/2022, 03/07/2022]  [07/06/2022, 03/07/2022]  $ 1200,0 reais

Información del DataFrame:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 30 entries, 0 to 29
Data columns (total 4 columns):
 #   Column                      Non-Null Count  Dtype 
---  ------                      --------------  ----- 
 0   apartamento                 30 non-null     object
 1   datas_combinadas_pagamento  30 non-null     object
 2   datas_de_pagamento          30 non-null     object
 3   valor_aluguel               30 non-null     object
dtypes: object(4)
memory usage: 1.1+ KB
None

Columna 'valor_aluguel':
0     $ 1000,0 reais
1     $ 2500,0 reais
2     $ 1100,0 reais
3     $ 2600,0 reais
4     $ 1200,0 reais
5     $ 2700,0 reais
6     $ 1300,0 reais
7     $ 2800,0 reais
8     $ 1400,0 reais
9     $ 2900,0 reais
10    $ 1500,0 reais
11    $ 1200,0 reais
12    $ 1600,0 reais
13    $ 1300,0 reais
14    $ 1700,0 reais
15    $ 1400,0 reais
16    $ 1800,0 reais
17    $ 1500,0 reais
18    $ 1900,0 reais
19    $ 1600,0 reais
20    $ 2000,0 reais
21    $ 1000,0 reais
22    $ 2100,0 reais
23    $ 1100,0 reais
24    $ 2200,0 reais
25    $ 1200,0 reais
26    $ 2300,0 reais
27    $ 2100,0 reais
28    $ 2400,0 reais
29    $ 2200,0 reais
Name: valor_aluguel, dtype: object

Información del DataFrame después de la transformación:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 30 entries, 0 to 29
Data columns (total 4 columns):
 #   Column                      Non-Null Count  Dtype  
---  ------                      --------------  -----  
 0   apartamento                 30 non-null     object 
 1   datas_combinadas_pagamento  30 non-null     object 
 2   datas_de_pagamento          30 non-null     object 
 3   valor_aluguel               30 non-null     float64
dtypes: float64(1), object(3)
memory usage: 1.1+ KB
None

Primeras filas del DataFrame después de la transformación:
      apartamento datas_combinadas_pagamento        datas_de_pagamento  valor_aluguel
0  A101 (blocoAP)   [01/06/2022, 01/07/2022]  [05/06/2022, 03/07/2022]         1000.0
1  A101 (blocoAP)   [01/06/2022, 01/07/2022]  [05/06/2022, 03/07/2022]         2500.0
2  A102 (blocoAP)   [02/06/2022, 02/07/2022]  [02/06/2022, 06/07/2022]         1100.0
3  A102 (blocoAP)   [02/06/2022, 02/07/2022]  [02/06/2022, 06/07/2022]         2600.0
4  B201 (blocoAP)   [03/06/2022, 03/07/2022]  [07/06/2022, 03/07/2022]         1200.0



Explicación del Código:
Normalizar la columna dados_locacao:

datos = pd.json_normalize(datos['dados_locacao']): Normaliza la columna dados_locacao para convertirla en un DataFrame.
Destrincar las listas con explode:

datos = datos.explode('valor_aluguel'): Expande la columna valor_aluguel para que cada elemento de la lista tenga su propia fila.
Resetear los índices de las líneas:

datos.reset_index(drop=True, inplace=True): Resetea el índice del DataFrame para que sea secuencial.
Transformar la columna numérica a tipo numérico:

datos['valor_aluguel'] = datos['valor_aluguel'].apply(lambda x: x.replace('$ ', '').replace(' reais', '').replace(',', '.').strip()): Limpia la columna valor_aluguel eliminando el símbolo $ y cambiando las comas por puntos.
datos['valor_aluguel'] = datos['valor_aluguel'].astype(np.float64): Convierte la columna valor_aluguel a tipo float64.

'''
# Convertir las columnas de fechas a tipo datetime
datos['datas_combinadas_pagamento'] = datos['datas_combinadas_pagamento'].apply(lambda x: pd.to_datetime(x, format='%d/%m/%Y'))
datos['datas_de_pagamento'] = datos['datas_de_pagamento'].apply(lambda x: pd.to_datetime(x, format='%d/%m/%Y'))

print("\nInformación del DataFrame después de convertir las fechas:")
print(datos.info())
'''
Información del DataFrame después de convertir las fechas:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 30 entries, 0 to 29
Data columns (total 4 columns):
 #   Column                      Non-Null Count  Dtype  
---  ------                      --------------  -----  
 0   apartamento                 30 non-null     object 
 1   datas_combinadas_pagamento  30 non-null     object 
 2   datas_de_pagamento          30 non-null     object 
 3   valor_aluguel               30 non-null     float64
dtypes: float64(1), object(3)
memory usage: 1.1+ KB
None
'''