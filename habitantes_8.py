import pandas as pd

# Leer las tablas del archivo HTML
datos_html = pd.read_html('habitantes.html')

# Seleccionar la tabla específica (índice 5 en este caso)
habitantes = datos_html[5]

# Renombrar las columnas para facilitar el acceso a los datos
habitantes.columns = ['N.º', 'País', 'Población', '% del total mundial']

# Limpiar y convertir la columna 'Población' a tipo entero
habitantes['Población'] = habitantes['Población'].str.replace('\xa0', '').str.replace(' ', '').astype(int)

# Imprimir las primeras filas del DataFrame
print("Primeras filas del DataFrame:")
print(habitantes.head())

# Imprimir información sobre el DataFrame
print("\nInformación del DataFrame:")
print(habitantes.info())

# Imprimir estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(habitantes.describe())

# Filtrar países con una población mayor a un cierto valor
poblacion_umbral = 100000000
paises_grandes = habitantes[habitantes['Población'] > poblacion_umbral]
print(f"\nPaíses con población mayor a {poblacion_umbral}:")
print(paises_grandes)

# Ordenar países por población
habitantes_ordenados = habitantes.sort_values(by='Población', ascending=False)
print("\nPaíses ordenados por población:")
print(habitantes_ordenados.head(10))

'''
Primeras filas del DataFrame:
  N.º            País   Población  % del total mundial
0   1           China  1264099000                 2056
1   2           India  1059634000                 1723
2   3  Estados Unidos   282399000                  459
3   4       Indonesia   214072000                  348
4   5          Brasil   175874000                  286

Información del DataFrame:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 238 entries, 0 to 237
Data columns (total 4 columns):
 #   Column               Non-Null Count  Dtype 
---  ------               --------------  ----- 
 0   N.º                  238 non-null    object
 1   País                 238 non-null    object
 2   Población            238 non-null    int64 
 3   % del total mundial  238 non-null    int64 
dtypes: int64(2), object(2)
memory usage: 7.6+ KB
None

Estadísticas descriptivas:
          Población  % del total mundial
count  2.380000e+02           238.000000
mean   2.586154e+10            83.991597
std    3.985722e+11           670.147871
min    1.000000e+03             0.000000
25%    2.935000e+05             0.250000
50%    4.258500e+06             7.000000
75%    1.576225e+07            25.750000
max    6.148898e+12         10000.000000

Países con población mayor a 100000000:
    N.º            País      Población  % del total mundial
0     1           China     1264099000                 2056
1     2           India     1059634000                 1723
2     3  Estados Unidos      282399000                  459
3     4       Indonesia      214072000                  348
4     5          Brasil      175874000                  286
5     6        Pakistán      154370000                  251
6     7           Rusia      146845000                  239
7     8       Bangladés      129193000                  210
8     9           Japón      126804000                  206
9    10         Nigeria      122852000                  200
237   -           Mundo  6148898000000                10000

Países ordenados por población:
    N.º            País      Población  % del total mundial
237   -           Mundo  6148898000000                10000
0     1           China     1264099000                 2056
1     2           India     1059634000                 1723
2     3  Estados Unidos      282399000                  459
3     4       Indonesia      214072000                  348
4     5          Brasil      175874000                  286
5     6        Pakistán      154370000                  251
6     7           Rusia      146845000                  239
7     8       Bangladés      129193000                  210
8     9           Japón      126804000                  206
'''