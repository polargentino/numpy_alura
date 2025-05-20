import pandas as pd

datos = pd.read_json('datos_hosting.json')
print(datos.head())

'''
                                      info_inmuebles
0  {'evaluacion_general': '10.0', 'experiencia_lo...
1  {'evaluacion_general': '10.0', 'experiencia_lo...
2  {'evaluacion_general': '10.0', 'experiencia_lo...
3  {'evaluacion_general': '10.0', 'experiencia_lo...
4  {'evaluacion_general': '10.0', 'experiencia_lo...
'''
datos = pd.json_normalize(datos['info_inmuebles'])
print(datos.head())
print(type(datos))
'''
 evaluacion_general  ...                                             precio
0               10.0  ...  [$110.00, $45.00, $55.00, $52.00, $85.00, $50....
1               10.0  ...  [$350.00, $300.00, $425.00, $300.00, $285.00, ...
2               10.0  ...                                          [$975.00]
3               10.0  ...  [$490.00, $550.00, $350.00, $350.00, $350.00, ...
4               10.0  ...                                 [$200.00, $545.00]
[5 rows x 13 columns]

<class 'pandas.core.frame.DataFrame'>
'''
columnas = list(datos.columns)
print(columnas)
'''
['evaluacion_general', 'experiencia_local', 'max_hospedes', 'descripcion_local', 
'descripcion_vecindad', 'cantidad_baños', 'cantidad_cuartos', 'cantidad_camas', 
'modelo_cama', 'comodidades', 'cuota_deposito', 'cuota_limpieza', 'precio']
'''
datos = datos.explode(columnas[3:])
print(datos)
'''
 evaluacion_general experiencia_local max_hospedes  ... cuota_deposito cuota_limpieza   precio
0                10.0                --            1  ...             $0             $0  $110.00
0                10.0                --            1  ...             $0             $0   $45.00
0                10.0                --            1  ...             $0             $0   $55.00
0                10.0                --            1  ...             $0         $20.00   $52.00
0                10.0                --            1  ...             $0         $15.00   $85.00
..                ...               ...          ...  ...            ...            ...      ...
68                nan                --            8  ...      $1,000.00        $178.00  $299.00
68                nan                --            8  ...             $0         $99.00  $199.00
68                nan                --            8  ...             $0             $0  $400.00
69                nan                --            9  ...      $1,000.00        $150.00  $250.00
69                nan                --            9  ...        $500.00             $0  $350.00

[3818 rows x 13 columns]
'''
datos.reset_index(inplace=True, drop=True)
print(datos.head())
'''
evaluacion_general experiencia_local max_hospedes  ... cuota_deposito cuota_limpieza   precio
0               10.0                --            1  ...             $0             $0  $110.00
1               10.0                --            1  ...             $0             $0   $45.00
2               10.0                --            1  ...             $0             $0   $55.00
3               10.0                --            1  ...             $0         $20.00   $52.00
4               10.0                --            1  ...             $0         $15.00   $85.00

[5 rows x 13 columns]
'''
print(datos.info())
'''
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
print(datos['precio'])
'''
None
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