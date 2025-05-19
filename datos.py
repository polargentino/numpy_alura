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