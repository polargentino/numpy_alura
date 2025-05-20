import pandas as pd

df_data = pd.read_json('datos_hosting.json')
print("Primeras filas del DataFrame:")
print(df_data.head())
print("\nInformación general del DataFrame:")
print(df_data.info())

'''
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


Primeras filas del DataFrame:
                                      info_inmuebles
0  {'evaluacion_general': '10.0', 'experiencia_lo...
1  {'evaluacion_general': '10.0', 'experiencia_lo...
2  {'evaluacion_general': '10.0', 'experiencia_lo...
3  {'evaluacion_general': '10.0', 'experiencia_lo...
4  {'evaluacion_general': '10.0', 'experiencia_lo...

Información general del DataFrame:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 70 entries, 0 to 69
Data columns (total 1 columns):
 #   Column          Non-Null Count  Dtype 
---  ------          --------------  ----- 
 0   info_inmuebles  70 non-null     object
dtypes: object(1)
memory usage: 688.0+ bytes
None
'''
df_normalizado = pd.json_normalize(df_data['info_inmuebles'])
print("DataFrame normalizado:")
print(df_normalizado.head())
print("\nInformación del DataFrame normalizado:")
print(df_normalizado.info())
'''
DataFrame normalizado:
  evaluacion_general  ...                                             precio
0               10.0  ...  [$110.00, $45.00, $55.00, $52.00, $85.00, $50....
1               10.0  ...  [$350.00, $300.00, $425.00, $300.00, $285.00, ...
2               10.0  ...                                          [$975.00]
3               10.0  ...  [$490.00, $550.00, $350.00, $350.00, $350.00, ...
4               10.0  ...                                 [$200.00, $545.00]

[5 rows x 13 columns]

Información del DataFrame normalizado:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 70 entries, 0 to 69
Data columns (total 13 columns):
 #   Column                Non-Null Count  Dtype 
---  ------                --------------  ----- 
 0   evaluacion_general    70 non-null     object
 1   experiencia_local     70 non-null     object
 2   max_hospedes          70 non-null     object
 3   descripcion_local     70 non-null     object
 4   descripcion_vecindad  70 non-null     object
 5   cantidad_baños        70 non-null     object
 6   cantidad_cuartos      70 non-null     object
 7   cantidad_camas        70 non-null     object
 8   modelo_cama           70 non-null     object
 9   comodidades           70 non-null     object
 10  cuota_deposito        70 non-null     object
 11  cuota_limpieza        70 non-null     object
 12  precio                70 non-null     object
dtypes: object(13)
memory usage: 7.2+ KB
None


Excelente! Ahora tenemos un DataFrame más estructurado. Observando la salida, podemos identificar 
varios puntos para trabajar:

Tipos de datos: Muchas columnas que deberían ser numéricas (como evaluacion_general, max_hospedes, 
cantidad_baños, cantidad_cuartos, cantidad_camas, cuota_deposito, cuota_limpieza) son de tipo object. 
Necesitaremos transformarlas a tipos numéricos.
Listas en la columna 'precio': La columna precio contiene listas de strings. Para analizar los 
precios individualmente, necesitaremos usar explode para que cada precio en la lista ocupe una fila 
separada.
Formato de los precios: Los precios en la lista de la columna precio vienen con el símbolo '$'. 
Necesitaremos remover este símbolo antes de convertirlos a números.
La columna 'comodidades' contiene listas: Podríamos querer analizar las comodidades individualmente, 
lo que requeriría usar explode.


Entendido. Siguiendo el orden de los temas que me proporcionaste, ya hemos cubierto el punto 1 
(a, b y c) al leer el JSON, identificar los ajustes necesarios y normalizar los datos. 
El punto 1d ("Comprender el problema de la fijación de precios inteligente") es más conceptual y lo 
podemos discutir una vez que hayamos trabajado con los datos de precios.
'''


'''
Ahora vamos al punto 2. Empecemos por el inciso 2a: Identificar y transformar elementos dentro de 
las listas en una nueva línea del DataFrame con explode. Vamos a aplicar esto a la columna 'precio'.

'''
df_precios_expandido = df_normalizado.explode('precio')
print("DataFrame con la columna 'precio' expandida:")
print(df_precios_expandido.head())
print("\nInformación del DataFrame con 'precio' expandido:")
print(df_precios_expandido.info())

'''
DataFrame con la columna 'precio' expandida:
  evaluacion_general experiencia_local  ...                                     cuota_limpieza   precio
0               10.0                --  ...  [$0, $0, $0, $20.00, $15.00, $28.00, $35.00, $...  $110.00
0               10.0                --  ...  [$0, $0, $0, $20.00, $15.00, $28.00, $35.00, $...   $45.00
0               10.0                --  ...  [$0, $0, $0, $20.00, $15.00, $28.00, $35.00, $...   $55.00
0               10.0                --  ...  [$0, $0, $0, $20.00, $15.00, $28.00, $35.00, $...   $52.00
0               10.0                --  ...  [$0, $0, $0, $20.00, $15.00, $28.00, $35.00, $...   $85.00

[5 rows x 13 columns]

Información del DataFrame con 'precio' expandido:
<class 'pandas.core.frame.DataFrame'>
Index: 3818 entries, 0 to 69
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
memory usage: 417.6+ KB
None


Excelente! Como ves, la columna 'precio' ahora tiene cada precio en una fila separada, lo cual nos 
permitirá trabajar con ellos individualmente.

Ahora vamos al punto 2b: Transformar datos textuales en datos numéricos con el método astype. Antes 
de usar astype, necesitamos limpiar la columna 'precio' removiendo el símbolo '$'. Podemos hacer 
esto usando el método str.replace().
'''
df_precios_expandido['precio'] = df_precios_expandido['precio'].str.replace('$', '', regex=False).str.replace(',', '', regex=False)

# Ahora intentamos convertir la columna 'precio' a numérico (float)
try:
    df_precios_expandido['precio'] = df_precios_expandido['precio'].astype(float)
    print("\nColumna 'precio' convertida a numérico:")
    print(df_precios_expandido['precio'].head())
    print("\nInformación actualizada del DataFrame:")
    print(df_precios_expandido.info())
except ValueError as e:
    print(f"Error al convertir a numérico: {e}")
    print("Revisando valores no numéricos en la columna 'precio':")
    print(df_precios_expandido[pd.to_numeric(df_precios_expandido['precio'], errors='coerce').isna()]['precio'].unique())

'''
Columna 'precio' convertida a numérico:
0    110.0
0     45.0
0     55.0
0     52.0
0     85.0
Name: precio, dtype: float64

Información actualizada del DataFrame:
<class 'pandas.core.frame.DataFrame'>
Index: 3818 entries, 0 to 69
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
 12  precio                3818 non-null   float64
dtypes: float64(1), object(12)
memory usage: 417.6+ KB
None


¡Perfecto! La columna 'precio' ahora es de tipo float64. Hemos cubierto el punto 2b.

Ahora vamos al punto 2c: Tratar los textos con datos numéricos para transformarlos con apply.

Tenemos varias columnas que deberían ser numéricas pero son de tipo object (por ejemplo, 
evaluacion_general, max_hospedes, cantidad_baños, cantidad_cuartos, cantidad_camas, cuota_deposito, 
cuota_limpieza). Algunas de estas podrían tener formatos de texto que necesiten ser limpiados antes 
de la conversión.

Vamos a intentar convertir algunas de estas columnas a numérico usando astype. Si encontramos 
errores (como antes con la coma), usaremos apply para definir una función de limpieza y luego 
convertiremos el resultado.

Empecemos con la columna evaluacion_general. Parece que ya está en un formato numérico como string 
(e.g., '10.0'). Podemos intentar convertirla directamente con astype.
'''