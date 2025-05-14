import pandas as pd

datos_pacientes = pd.read_json('pacientes.json')
print(datos_pacientes)

'''
     ID_paciente Enfermedad_corazon    IMC Fumador  ... Horas_sueño Asma  Enfermedad_renal  Cancer_piel
0              0                 No  16.60      Sí  ...           5   Sí                No           Sí
1              1                 No  20.34      No  ...           7   No                No           No
2              2                 No  26.58      Sí  ...           8   Sí                No           No
3              3                 No  24.21      No  ...           6   No                No           Sí
4              4                 No  23.71      No  ...           8   No                No           No
..           ...                ...    ...     ...  ...         ...  ...               ...          ...
995          995                 No  28.29      Sí  ...           8   No                No           No
996          996                 No  25.69      Sí  ...           8   No                No           No
997          997                 Sí  26.99      No  ...           8   No                No           No
998          998                 No  44.29      No  ...           6   Sí                No           No
999          999                 No  25.83      No  ...           7   No                No           No

[1000 rows x 19 columns]
'''
datos_pacientes_2 = pd.read_json('pacientes_2.json')
print(datos_pacientes_2.head())

'''
                                 Investigación   Año                                          Pacientes
0  Indicadores clave de enfermedades cardíacas  2020  {'ID': '01', 'Rango_edad': '55-59', 'Sexo_biol...
1  Indicadores clave de enfermedades cardíacas  2020  {'ID': '02', 'Rango_edad': '80 ó +', 'Sexo_bio...
2  Indicadores clave de enfermedades cardíacas  2020  {'ID': '03', 'Rango_edad': '65-69', 'Sexo_biol..
'''