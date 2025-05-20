import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo JSON
datos = pd.read_json('datos_hosting.json')

# Mostrar las primeras filas del DataFrame
print("Primeras filas del DataFrame original:")
print(datos.head())
'''
Primeras filas del DataFrame original:
                                      info_inmuebles
0  {'evaluacion_general': '10.0', 'experiencia_lo...
1  {'evaluacion_general': '10.0', 'experiencia_lo...
2  {'evaluacion_general': '10.0', 'experiencia_lo...
3  {'evaluacion_general': '10.0', 'experiencia_lo...
4  {'evaluacion_general': '10.0', 'experiencia_lo...
'''
# Normalizar la columna 'info_inmuebles'
datos = pd.json_normalize(datos['info_inmuebles'])

# Mostrar las primeras filas del DataFrame normalizado
print("\nPrimeras filas del DataFrame normalizado:")
print(datos.head())
'''
Primeras filas del DataFrame normalizado:
  evaluacion_general  ...                                             precio
0               10.0  ...  [$110.00, $45.00, $55.00, $52.00, $85.00, $50....
1               10.0  ...  [$350.00, $300.00, $425.00, $300.00, $285.00, ...
2               10.0  ...                                          [$975.00]
3               10.0  ...  [$490.00, $550.00, $350.00, $350.00, $350.00, ...
4               10.0  ...                                 [$200.00, $545.00]

[5 rows x 13 columns]
'''
# Mostrar el tipo del DataFrame
print("\nTipo del DataFrame:")
print(type(datos))
'''
Tipo del DataFrame:
<class 'pandas.core.frame.DataFrame'>
'''
# Obtener la lista de columnas
columnas = list(datos.columns)
print("\nColumnas del DataFrame:")
print(columnas)
'''
Columnas del DataFrame:
['evaluacion_general', 'experiencia_local', 'max_hospedes', 'descripcion_local', 
'descripcion_vecindad', 'cantidad_baños', 'cantidad_cuartos', 'cantidad_camas', 'modelo_cama', 
'comodidades', 'cuota_deposito', 'cuota_limpieza', 'precio']
'''
# Explode las columnas que contienen listas
datos = datos.explode(columnas[3:])

# Mostrar las primeras filas del DataFrame después de explode
print("\nPrimeras filas del DataFrame después de explode:")
print(datos.head())
'''
Primeras filas del DataFrame después de explode:
  evaluacion_general experiencia_local max_hospedes  ... cuota_deposito cuota_limpieza   precio
0               10.0                --            1  ...             $0             $0  $110.00
0               10.0                --            1  ...             $0             $0   $45.00
0               10.0                --            1  ...             $0             $0   $55.00
0               10.0                --            1  ...             $0         $20.00   $52.00
0               10.0                --            1  ...             $0         $15.00   $85.00

[5 rows x 13 columns]
'''
# Resetear el índice del DataFrame
datos.reset_index(inplace=True, drop=True)

# Mostrar las primeras filas del DataFrame después de resetear el índice
print("\nPrimeras filas del DataFrame después de resetear el índice:")
print(datos.head())
'''
Primeras filas del DataFrame después de resetear el índice:
  evaluacion_general experiencia_local max_hospedes  ... cuota_deposito cuota_limpieza   precio
0               10.0                --            1  ...             $0             $0  $110.00
1               10.0                --            1  ...             $0             $0   $45.00
2               10.0                --            1  ...             $0             $0   $55.00
3               10.0                --            1  ...             $0         $20.00   $52.00
4               10.0                --            1  ...             $0         $15.00   $85.00

[5 rows x 13 columns]
'''
# Mostrar información del DataFrame
print("\nInformación del DataFrame:")
print(datos.info())
'''
Información del DataFrame:
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
None

'''
# Mostrar la columna 'precio'
print("\nColumna 'precio':")
print(datos['precio'])
'''
Columna 'precio':
0       $110.00
1        $45.00
2        $55.00
3        $52.00
4        $85.00
         ...   
3813    $299.00
3814    $199.00
3815    $400.00
3816    $250.00
3817    $350.00
Name: precio, Length: 3818, dtype: object
'''
# Limpiar la columna 'precio' eliminando el símbolo '$' y las comas
datos['precio'] = datos['precio'].apply(lambda x: x.replace('$', '').replace(',', '').strip())

# Mostrar la columna 'precio' después de limpiar
print("\nColumna 'precio' después de limpiar:")
print(datos['precio'])
'''
Columna 'precio' después de limpiar:
0       110.00
1        45.00
2        55.00
3        52.00
4        85.00
         ...  
3813    299.00
3814    199.00
3815    400.00
3816    250.00
3817    350.00
Name: precio, Length: 3818, dtype: object
'''
# Convertir la columna 'precio' a tipo numérico
datos['precio'] = pd.to_numeric(datos['precio'], errors='coerce')

# Mostrar la columna 'precio' después de convertir a numérico
print("\nColumna 'precio' después de convertir a numérico:")
print(datos['precio'])
'''
Columna 'precio' después de convertir a numérico:
0       110.0
1        45.0
2        55.0
3        52.0
4        85.0
        ...  
3813    299.0
3814    199.0
3815    400.0
3816    250.0
3817    350.0
Name: precio, Length: 3818, dtype: float64
'''
# Mostrar las columnas 'cuota_deposito' y 'cuota_limpieza'
print("\nColumnas 'cuota_deposito' y 'cuota_limpieza':")
print(datos[['cuota_deposito', 'cuota_limpieza']])
'''
Columnas 'cuota_deposito' y 'cuota_limpieza':
     cuota_deposito cuota_limpieza
0                $0             $0
1                $0             $0
2                $0             $0
3                $0         $20.00
4                $0         $15.00
...             ...            ...
3813      $1,000.00        $178.00
3814             $0         $99.00
3815             $0             $0
3816      $1,000.00        $150.00
3817        $500.00             $0

[3818 rows x 2 columns]
'''
# Limpiar y convertir 'cuota_deposito' y 'cuota_limpieza' a tipo numérico
datos['cuota_deposito'] = datos['cuota_deposito'].apply(lambda x: x.replace('$', '').replace(',', '').strip())
datos['cuota_limpieza'] = datos['cuota_limpieza'].apply(lambda x: x.replace('$', '').replace(',', '').strip())

datos['cuota_deposito'] = pd.to_numeric(datos['cuota_deposito'], errors='coerce')
datos['cuota_limpieza'] = pd.to_numeric(datos['cuota_limpieza'], errors='coerce')

print("\nColumnas 'cuota_deposito' y 'cuota_limpieza' después de convertir a numérico:")
print(datos[['cuota_deposito', 'cuota_limpieza']])
'''

Columnas 'cuota_deposito' y 'cuota_limpieza' después de convertir a numérico:
      cuota_deposito  cuota_limpieza
0                0.0             0.0
1                0.0             0.0
2                0.0             0.0
3                0.0            20.0
4                0.0            15.0
...              ...             ...
3813          1000.0           178.0
3814             0.0            99.0
3815             0.0             0.0
3816          1000.0           150.0
3817           500.0             0.0

[3818 rows x 2 columns]
'''
# Calcular estadísticas descriptivas para las columnas numéricas
print("\nEstadísticas descriptivas para las columnas numéricas:")
print(datos[['precio', 'cuota_deposito', 'cuota_limpieza']].describe())
'''
Estadísticas descriptivas para las columnas numéricas:
            precio  cuota_deposito  cuota_limpieza
count  3818.000000     3818.000000     3818.000000
mean    127.976166      140.566003       45.062860
std      90.250022      237.387534       49.913798
min      20.000000        0.000000        0.000000
25%      75.000000        0.000000        0.000000
50%     100.000000        0.000000       30.000000
75%     150.000000      200.000000       65.000000
max    1000.000000     5000.000000      300.000000
'''

# Mostrar información del DataFrame
print("\nInformación del DataFrame:")
print(datos.info())
'''

Información del DataFrame:
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
 10  cuota_deposito        3818 non-null   float64
 11  cuota_limpieza        3818 non-null   float64
 12  precio                3818 non-null   float64
dtypes: float64(3), object(10)
memory usage: 387.9+ KB
None
'''
# Convertir 'evaluacion_general' a tipo numérico
datos['evaluacion_general'] = pd.to_numeric(datos['evaluacion_general'], errors='coerce')

# Convertir 'max_hospedes' a tipo numérico
datos['max_hospedes'] = pd.to_numeric(datos['max_hospedes'], errors='coerce')

# Convertir 'cantidad_baños' a tipo numérico
datos['cantidad_baños'] = pd.to_numeric(datos['cantidad_baños'], errors='coerce')

# Convertir 'cantidad_cuartos' a tipo numérico
datos['cantidad_cuartos'] = pd.to_numeric(datos['cantidad_cuartos'], errors='coerce')

# Convertir 'cantidad_camas' a tipo numérico
datos['cantidad_camas'] = pd.to_numeric(datos['cantidad_camas'], errors='coerce')

# Mostrar la información del DataFrame después de la conversión
print("\nInformación del DataFrame después de la conversión:")
print(datos.info())
'''
Información del DataFrame después de la conversión:
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
None


Tipos de Datos y Conversiones
Columnas Convertidas a float64:

evaluacion_general: Convertida a float64 porque contiene valores numéricos con decimales.
cuota_deposito: Convertida a float64 porque puede contener valores numéricos con decimales.
cuota_limpieza: Convertida a float64 porque puede contener valores numéricos con decimales.
precio: Convertida a float64 porque puede contener valores numéricos con decimales.
Columnas Convertidas a int64:

max_hospedes: Convertida a int64 porque contiene valores enteros.
cantidad_baños: Convertida a int64 porque contiene valores enteros.
cantidad_cuartos: Convertida a int64 porque contiene valores enteros.
cantidad_camas: Convertida a int64 porque contiene valores enteros.
Columnas de tipo object:

experiencia_local: Se mantiene como object porque contiene texto o valores categóricos.
descripcion_local: Se mantiene como object porque contiene texto.
descripcion_vecindad: Se mantiene como object porque contiene texto.
modelo_cama: Se mantiene como object porque contiene texto o valores categóricos.
comodidades: Se mantiene como object porque contiene texto o valores categóricos.
Explicación de las Conversiones
pd.to_numeric(): Esta función convierte una columna a un tipo numérico. El parámetro errors='coerce' convierte cualquier valor no numérico a NaN, lo que es útil para manejar datos inconsistentes.
float64 vs int64: float64 se utiliza para valores numéricos con decimales, mientras que int64 se utiliza para valores enteros
'''
# Crear un histograma de los precios
plt.hist(datos['precio'].dropna(), bins=20)
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
plt.title('Distribución de Precios')
plt.show()

# Crear un gráfico de barras para la cantidad de baños
plt.hist(datos['cantidad_baños'].dropna(), bins=10)
plt.xlabel('Cantidad de Baños')
plt.ylabel('Frecuencia')
plt.title('Distribución de Cantidad de Baños')
plt.show()
'''
Explicación del Código de Visualización:
plt.hist(): Crea un histograma de los datos.
plt.xlabel() y plt.ylabel(): Establecen las etiquetas de los ejes x e y.
plt.title(): Establece el título del gráfico.
plt.show(): Muestra el gráfico.

'''
print("\nColumna 'descripcion_local':")
print(datos['descripcion_local'])
'''

Columna 'descripcion_local':
0       This clean and comfortable one bedroom sits ri...
1       Our century old Upper Queen Anne house is loca...
2       Cozy room in two-bedroom apartment along the l...
3       Very lovely and cozy room for one. Convenientl...
4       The “Studio at Mibbett Hollow' is in a Beautif...
                              ...                        
3813    Beautiful craftsman home in the historic Wedgw...
3814    Located in a very easily accessible area of Se...
3815    This home is fully furnished and available wee...
3816    This business-themed modern home features:  *H...
3817    This welcoming home is in the quiet residentia...
Name: descripcion_local, Length: 3818, dtype: object
'''
print("\nColumna 'descripcion_local':")
print(datos['descripcion_local'].str.lower())
'''

Columna 'descripcion_local':
0       this clean and comfortable one bedroom sits ri...
1       our century old upper queen anne house is loca...
2       cozy room in two-bedroom apartment along the l...
3       very lovely and cozy room for one. convenientl...
4       the “studio at mibbett hollow' is in a beautif...
                              ...                        
3813    beautiful craftsman home in the historic wedgw...
3814    located in a very easily accessible area of se...
3815    this home is fully furnished and available wee...
3816    this business-themed modern home features:  *h...
3817    this welcoming home is in the quiet residentia...
Name: descripcion_local, Length: 3818, dtype: object
'''
datos['descripcion_local'] = datos['descripcion_local'].str.lower()
print(datos.head())
'''
 evaluacion_general experiencia_local  max_hospedes  ... cuota_deposito cuota_limpieza  precio
0                10.0                --             1  ...            0.0            0.0   110.0
1                10.0                --             1  ...            0.0            0.0    45.0
2                10.0                --             1  ...            0.0            0.0    55.0
3                10.0                --             1  ...            0.0           20.0    52.0
4                10.0                --             1  ...            0.0           15.0    85.0
[5 rows x 13 columns]
'''

print(datos['descripcion_local'][3169])
'''
built, run and supported by seattle tech and start up veterans, grokhome's focus is to create a 
supportive environment for smart people working on interesting projects, start ups and more. this 
listing is an upper bunk, in a 2-person shared room. *note: this fall, there will be major 
renovations happening on one kitchen and bathroom at a time. there will always be two other 
working kitchens and two working bathrooms in the house. we'll work to minimize the impact these 
renovations have on your stay. **this listing is only available to those working in the tech/science 
space. live in a hacker house, and immerse yourself in the seattle tech scene. you can expect to 
be surrounded by smart people solving big problems or working on something fun. we have frequent 
demo nights, and love when our guests share something they are passionate about. if you're new to 
the city, our deep ties to the seattle tech scene can help you get involved. expand your network,
 develop your ideas, and learn somet
'''
