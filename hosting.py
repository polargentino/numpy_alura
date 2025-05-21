
'''
datos_hosting.json de Google Colab - ─(pol㉿kali)-[~/Descargas/2071-ProyectoFinal/data]
└─$ ls
datos_hosting.json 

Ayuda de Gemini AI:
-------------------
Temas: 

1)-

a- Leer archivos de datos con read_json;

b- Identificar los ajustes necesarios para un posterior procesamiento en un conjunto de datos;

c- Normalizar la visualización de los datos con el método json_normalize;

d- Comprender el problema de la fijación de precios inteligente.

2)-

a- Identificar y transformar elementos dentro de las listas en una nueva línea del DataFrame 
con explode;

b- Transformar datos textuales en datos numéricos con el método astype;

c- Tratar los textos con datos numéricos para transformarlos con apply;

d- Tratar varias columnas elemento por elemento con applymap.

3)-

a- Manipular elementos textuales en un DataFrame;

b- Trabajar con expresiones regulares (regex) para tratar el texto;

c- Transformar textos en listas;

d- Realizar el proceso de tokenización de strings.

4)-

a- Identificar el tipo de datos datetime;

b- Transformar datos para el tipo datetime y

c- Manipular columnas de tipo datetime a través de métodos. 
'''

import pandas as pd
import numpy as np

# 1a- Leer archivos de datos con read_json;
datos = pd.read_json('datos_hosting.json')
print("Primeras filas del DataFrame original:")
print(datos.head())
print("\n")

# Normalizar la columna 'info_inmuebles' que contiene diccionarios anidados
# 1c- Normalizar la visualización de los datos con el método json_normalize;
datos = pd.json_normalize(datos['info_inmuebles'])
print("Primeras filas del DataFrame normalizado:")
print(datos.head())
print("\n")

# Obtener la lista de todas las columnas del DataFrame normalizado
columnas = list(datos.columns)
print("Columnas del DataFrame normalizado:", columnas)
print("\n")

# 2a- Identificar y transformar elementos dentro de las listas en una nueva línea del DataFrame con explode;
# Aplicamos explode a todas las columnas a partir de la cuarta (índice 3).
# Esto desglosará las listas que puedan existir en estas columnas en filas separadas.
datos = datos.explode(columnas[3:])
print("DataFrame después de aplicar explode (a partir de la cuarta columna):")
print(datos.head())
print("\n")

# Resetear el índice del DataFrame después del explode
datos.reset_index(inplace = True, drop = True)
print("DataFrame con índice reseteado:")
print(datos.head())
print("\n")

# Información general del DataFrame después del explode
print("Información del DataFrame después del explode:")
datos.info()
print("\n")

# 2b- Transformar datos textuales en datos numéricos con el método astype;
# Convertir la columna 'max_hospedes' a tipo entero (int64)
datos['max_hospedes'] = datos['max_hospedes'].astype(np.int64)
print("Información del DataFrame después de convertir 'max_hospedes' a int64:")
datos.info()
print("\n")

# Convertir varias columnas numéricas a tipo entero (int64)
col_numericas = ['cantidad_baños', 'cantidad_cuartos', 'cantidad_camas']
datos[col_numericas] = datos[col_numericas].astype(np.int64)
print("Información del DataFrame después de convertir 'cantidad_baños', 'cantidad_cuartos', 'cantidad_camas' a int64:")
datos.info()
print("\n")

# Convertir la columna 'evaluacion_general' a tipo float (float64)
datos['evaluacion_general'] = datos['evaluacion_general'].astype(np.float64)
print("Información del DataFrame después de convertir 'evaluacion_general' a float64:")
datos.info()
print("\n")

# 2c- Tratar los textos con datos numéricos para transformarlos con apply;
# Remover el símbolo '$' y la coma de la columna 'precio' y luego convertirla a float
datos['precio'] = datos['precio'].apply(lambda x: x.replace('$','').replace(',','').strip())
datos['precio'] = datos['precio'].astype(np.float64)
print("Información del DataFrame después de limpiar y convertir 'precio' a float64:")
datos.info()
print("\n")

# 2d- Tratar varias columnas elemento por elemento con applymap.
# Remover el símbolo '$' y la coma de las columnas 'cuota_deposito' y 'cuota_limpieza'
datos[['cuota_deposito', 'cuota_limpieza']] = datos[['cuota_deposito', 'cuota_limpieza']].applymap(lambda x: x.replace('$','').replace(',','').strip())
# Convertir las columnas 'cuota_deposito' y 'cuota_limpieza' a tipo float
datos[['cuota_deposito', 'cuota_limpieza']] = datos[['cuota_deposito', 'cuota_limpieza']].astype(np.float64)
print("Información del DataFrame después de limpiar y convertir 'cuota_deposito' y 'cuota_limpieza' a float64:")
datos.info()
print("\n")

print("Primeras filas del DataFrame después de las conversiones numéricas:")
print(datos.head())
print("\n")

# 3a- Manipular elementos textuales en un DataFrame;
# Convertir la columna 'descripcion_local' a minúsculas
datos['descripcion_local'] = datos['descripcion_local'].str.lower()
print("Primeras filas de la columna 'descripcion_local' en minúsculas:")
print(datos['descripcion_local'].head())
print("\n")

# Ejemplo de un valor en la columna 'descripcion_local'
print("Ejemplo de descripción local (índice 3169):")
print(datos['descripcion_local'].iloc[3169])
print("\n")

# 3b- Trabajar con expresiones regulares (regex) para tratar el texto;
# Remover caracteres que no sean alfanuméricos, guiones o apóstrofes en 'descripcion_local'
datos['descripcion_local'] = datos['descripcion_local'].str.replace('[^a-zA-Z0-9\-\']',' ',regex=True)
# Remover guiones que no estén entre palabras en 'descripcion_local'
datos['descripcion_local'] = datos['descripcion_local'].str.replace('(?<!\w)-(?!\w)',' ',regex=True)
print("Primeras filas de 'descripcion_local' después de aplicar regex:")
print(datos['descripcion_local'].head())
print("\n")

# 3c- Transformar textos en listas;
# Dividir la columna 'descripcion_local' en listas de palabras
datos['descripcion_local'] = datos['descripcion_local'].str.split()
print("Primeras filas de 'descripcion_local' convertida a listas de palabras:")
print(datos.head())
print("\n")

# Manipular la columna 'comodidades'
datos['comodidades'] = datos['comodidades'].str.replace('\{|}|\"','', regex=True)
# 3d- Realizar el proceso de tokenización de strings.
# Dividir la columna 'comodidades' en listas de comodidades
datos['comodidades'] = datos['comodidades'].str.split(',')
print("Primeras filas de 'comodidades' convertida a listas:")
print(datos.head())

'''
Primeras filas del DataFrame original:
                                      info_inmuebles
0  {'evaluacion_general': '10.0', 'experiencia_lo...
1  {'evaluacion_general': '10.0', 'experiencia_lo...
2  {'evaluacion_general': '10.0', 'experiencia_lo...
3  {'evaluacion_general': '10.0', 'experiencia_lo...
4  {'evaluacion_general': '10.0', 'experiencia_lo...


Primeras filas del DataFrame normalizado:
  evaluacion_general  ...                                             precio
0               10.0  ...  [$110.00, $45.00, $55.00, $52.00, $85.00, $50....
1               10.0  ...  [$350.00, $300.00, $425.00, $300.00, $285.00, ...
2               10.0  ...                                          [$975.00]
3               10.0  ...  [$490.00, $550.00, $350.00, $350.00, $350.00, ...
4               10.0  ...                                 [$200.00, $545.00]

[5 rows x 13 columns]


Columnas del DataFrame normalizado: ['evaluacion_general', 'experiencia_local', 'max_hospedes', 'descripcion_local', 'descripcion_vecindad', 'cantidad_baños', 'cantidad_cuartos', 'cantidad_camas', 'modelo_cama', 'comodidades', 'cuota_deposito', 'cuota_limpieza', 'precio']


DataFrame después de aplicar explode (a partir de la cuarta columna):
  evaluacion_general experiencia_local max_hospedes  ... cuota_deposito cuota_limpieza   precio
0               10.0                --            1  ...             $0             $0  $110.00
0               10.0                --            1  ...             $0             $0   $45.00
0               10.0                --            1  ...             $0             $0   $55.00
0               10.0                --            1  ...             $0         $20.00   $52.00
0               10.0                --            1  ...             $0         $15.00   $85.00

[5 rows x 13 columns]


DataFrame con índice reseteado:
  evaluacion_general experiencia_local max_hospedes  ... cuota_deposito cuota_limpieza   precio
0               10.0                --            1  ...             $0             $0  $110.00
1               10.0                --            1  ...             $0             $0   $45.00
2               10.0                --            1  ...             $0             $0   $55.00
3               10.0                --            1  ...             $0         $20.00   $52.00
4               10.0                --            1  ...             $0         $15.00   $85.00

[5 rows x 13 columns]


Información del DataFrame después del explode:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3818 entries, 0 to 3817
Data columns (total 13 columns):
 #   Column                Non-Null Count  Dtype 
---  ------                --------------  ----- 
 0   evaluacion_general    3818 non-null   object
 1   experiencia_local     3818 non-null   object
 2   max_hospedes          3818 non-null   object
 3   descripcion_local     3818 non-null   object
 4   descripcion_vecindad  3818 non-null   object
 5   cantidad_baños        3818 non-null   object
 6   cantidad_cuartos      3818 non-null   object
 7   cantidad_camas        3818 non-null   object
 8   modelo_cama           3818 non-null   object
 9   comodidades           3818 non-null   object
 10  cuota_deposito        3818 non-null   object
 11  cuota_limpieza        3818 non-null   object
 12  precio                3818 non-null   object
dtypes: object(13)
memory usage: 387.9+ KB


Información del DataFrame después de convertir 'max_hospedes' a int64:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3818 entries, 0 to 3817
Data columns (total 13 columns):
 #   Column                Non-Null Count  Dtype 
---  ------                --------------  ----- 
 0   evaluacion_general    3818 non-null   object
 1   experiencia_local     3818 non-null   object
 2   max_hospedes          3818 non-null   int64 
 3   descripcion_local     3818 non-null   object
 4   descripcion_vecindad  3818 non-null   object
 5   cantidad_baños        3818 non-null   object
 6   cantidad_cuartos      3818 non-null   object
 7   cantidad_camas        3818 non-null   object
 8   modelo_cama           3818 non-null   object
 9   comodidades           3818 non-null   object
 10  cuota_deposito        3818 non-null   object
 11  cuota_limpieza        3818 non-null   object
 12  precio                3818 non-null   object
dtypes: int64(1), object(12)
memory usage: 387.9+ KB


Información del DataFrame después de convertir 'cantidad_baños', 'cantidad_cuartos', 'cantidad_camas' a int64:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3818 entries, 0 to 3817
Data columns (total 13 columns):
 #   Column                Non-Null Count  Dtype 
---  ------                --------------  ----- 
 0   evaluacion_general    3818 non-null   object
 1   experiencia_local     3818 non-null   object
 2   max_hospedes          3818 non-null   int64 
 3   descripcion_local     3818 non-null   object
 4   descripcion_vecindad  3818 non-null   object
 5   cantidad_baños        3818 non-null   int64 
 6   cantidad_cuartos      3818 non-null   int64 
 7   cantidad_camas        3818 non-null   int64 
 8   modelo_cama           3818 non-null   object
 9   comodidades           3818 non-null   object
 10  cuota_deposito        3818 non-null   object
 11  cuota_limpieza        3818 non-null   object
 12  precio                3818 non-null   object
dtypes: int64(4), object(9)
memory usage: 387.9+ KB


Información del DataFrame después de convertir 'evaluacion_general' a float64:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3818 entries, 0 to 3817
Data columns (total 13 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   evaluacion_general    3162 non-null   float64
 1   experiencia_local     3818 non-null   object 
 2   max_hospedes          3818 non-null   int64  
 3   descripcion_local     3818 non-null   object 
 4   descripcion_vecindad  3818 non-null   object 
 5   cantidad_baños        3818 non-null   int64  
 6   cantidad_cuartos      3818 non-null   int64  
 7   cantidad_camas        3818 non-null   int64  
 8   modelo_cama           3818 non-null   object 
 9   comodidades           3818 non-null   object 
 10  cuota_deposito        3818 non-null   object 
 11  cuota_limpieza        3818 non-null   object 
 12  precio                3818 non-null   object 
dtypes: float64(1), int64(4), object(8)
memory usage: 387.9+ KB


Información del DataFrame después de limpiar y convertir 'precio' a float64:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3818 entries, 0 to 3817
Data columns (total 13 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   evaluacion_general    3162 non-null   float64
 1   experiencia_local     3818 non-null   object 
 2   max_hospedes          3818 non-null   int64  
 3   descripcion_local     3818 non-null   object 
 4   descripcion_vecindad  3818 non-null   object 
 5   cantidad_baños        3818 non-null   int64  
 6   cantidad_cuartos      3818 non-null   int64  
 7   cantidad_camas        3818 non-null   int64  
 8   modelo_cama           3818 non-null   object 
 9   comodidades           3818 non-null   object 
 10  cuota_deposito        3818 non-null   object 
 11  cuota_limpieza        3818 non-null   object 
 12  precio                3818 non-null   float64
dtypes: float64(2), int64(4), object(7)
memory usage: 387.9+ KB


/home/pol/Escritorio/numpy_alura/hosting.py:117: FutureWarning: DataFrame.applymap has been deprecated. Use DataFrame.map instead.
  datos[['cuota_deposito', 'cuota_limpieza']] = datos[['cuota_deposito', 'cuota_limpieza']].applymap(lambda x: x.replace('$','').replace(',','').strip())
Información del DataFrame después de limpiar y convertir 'cuota_deposito' y 'cuota_limpieza' a float64:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3818 entries, 0 to 3817
Data columns (total 13 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   evaluacion_general    3162 non-null   float64
 1   experiencia_local     3818 non-null   object 
 2   max_hospedes          3818 non-null   int64  
 3   descripcion_local     3818 non-null   object 
 4   descripcion_vecindad  3818 non-null   object 
 5   cantidad_baños        3818 non-null   int64  
 6   cantidad_cuartos      3818 non-null   int64  
 7   cantidad_camas        3818 non-null   int64  
 8   modelo_cama           3818 non-null   object 
 9   comodidades           3818 non-null   object 
 10  cuota_deposito        3818 non-null   float64
 11  cuota_limpieza        3818 non-null   float64
 12  precio                3818 non-null   float64
dtypes: float64(4), int64(4), object(5)
memory usage: 387.9+ KB


Primeras filas del DataFrame después de las conversiones numéricas:
   evaluacion_general experiencia_local  max_hospedes  ... cuota_deposito cuota_limpieza  precio
0                10.0                --             1  ...            0.0            0.0   110.0
1                10.0                --             1  ...            0.0            0.0    45.0
2                10.0                --             1  ...            0.0            0.0    55.0
3                10.0                --             1  ...            0.0           20.0    52.0
4                10.0                --             1  ...            0.0           15.0    85.0

[5 rows x 13 columns]


Primeras filas de la columna 'descripcion_local' en minúsculas:
0    this clean and comfortable one bedroom sits ri...
1    our century old upper queen anne house is loca...
2    cozy room in two-bedroom apartment along the l...
3    very lovely and cozy room for one. convenientl...
4    the “studio at mibbett hollow' is in a beautif...
Name: descripcion_local, dtype: object


Ejemplo de descripción local (índice 3169):
built, run and supported by seattle tech and start up veterans, grokhome's focus is to create a supportive environment for smart people working on interesting projects, start ups and more. this listing is an upper bunk, in a 2-person shared room. *note: this fall, there will be major renovations happening on one kitchen and bathroom at a time. there will always be two other working kitchens and two working bathrooms in the house. we'll work to minimize the impact these renovations have on your stay. **this listing is only available to those working in the tech/science space. live in a hacker house, and immerse yourself in the seattle tech scene. you can expect to be surrounded by smart people solving big problems or working on something fun. we have frequent demo nights, and love when our guests share something they are passionate about. if you're new to the city, our deep ties to the seattle tech scene can help you get involved. expand your network, develop your ideas, and learn somet


Primeras filas de 'descripcion_local' después de aplicar regex:
0    this clean and comfortable one bedroom sits ri...
1    our century old upper queen anne house is loca...
2    cozy room in two-bedroom apartment along the l...
3    very lovely and cozy room for one  convenientl...
4    the  studio at mibbett hollow' is in a beautif...
Name: descripcion_local, dtype: object


Primeras filas de 'descripcion_local' convertida a listas de palabras:
   evaluacion_general experiencia_local  max_hospedes  ... cuota_deposito cuota_limpieza  precio
0                10.0                --             1  ...            0.0            0.0   110.0
1                10.0                --             1  ...            0.0            0.0    45.0
2                10.0                --             1  ...            0.0            0.0    55.0
3                10.0                --             1  ...            0.0           20.0    52.0
4                10.0                --             1  ...            0.0           15.0    85.0

[5 rows x 13 columns]


Primeras filas de 'comodidades' convertida a listas:
   evaluacion_general experiencia_local  max_hospedes  ... cuota_deposito cuota_limpieza  precio
0                10.0                --             1  ...            0.0            0.0   110.0
1                10.0                --             1  ...            0.0            0.0    45.0
2                10.0                --             1  ...            0.0            0.0    55.0
3                10.0                --             1  ...            0.0           20.0    52.0
4                10.0                --             1  ...            0.0           15.0    85.0

[5 rows x 13 columns]
                                                           



¡Excelente! Vemos que el código se ejecutó correctamente y realizamos todas las transformaciones solicitadas en los puntos 1, 2 y 3.

Ahora podemos abordar el punto 1d: Comprender el problema de la fijación de precios inteligente.

La fijación de precios inteligente (o smart pricing) es una estrategia en la que los precios de bienes o servicios se ajustan dinámicamente en respuesta a diversos factores, como la demanda del mercado, la oferta, los precios de la competencia, el tiempo (por ejemplo, precios más altos los fines de semana), el comportamiento del cliente y otros datos relevantes.

En el contexto de los alquileres de hosting (como los que estamos analizando), la fijación de precios inteligente podría implicar que el precio de una propiedad varíe según:

La temporada o la demanda: Precios más altos en temporadas altas de turismo o en fines de semana.
Eventos locales: Aumento de precios cuando hay eventos importantes cerca.
La ocupación: Ajustes para incentivar reservas si la ocupación es baja o para maximizar ingresos si es alta.
Precios de propiedades similares: Monitorear y reaccionar a los precios de la competencia.
El objetivo de la fijación de precios inteligente es maximizar los ingresos para el anfitrión, optimizando los precios en tiempo real para capturar la mayor disposición a pagar de los huéspedes en diferentes momentos y circunstancias.

¿Tiene sentido esta explicación inicial? ¿Hay algún aspecto específico de la fijación de precios inteligente que te gustaría explorar más?

Una vez que comprendamos esto, podemos pasar al punto 4 sobre el tipo de dato datetime. ¿Tienes alguna columna en este DataFrame que represente fechas? Si no, podemos crear una para practicar.
'''