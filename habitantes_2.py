import pandas as pd

datos_html = pd.read_html('habitantes.html')
habitantes = datos_html[1]
print(habitantes)

#print(datos_html)
print(type(datos_html))
print(len(datos_html))
'''
        Continente, subcontinente o región geográfica  ...  Años para even- tual dupli- ca- ción
0                                              África  ...                                    29
1                                      África Central  ...                                    28
2                                    África del Norte  ...                                    43
3                                      África del Sur  ...                                    44
4                                   África Occidental  ...                                    25
..                                                ...  ...                                   ...
92  Organización del Tratado del Atlántico Norte (...  ...                                   139
93                                      Países árabes  ...                                    36
94                               Próximos once (N-11)  ...                                    46
95                       Unión Económica Euroasiática  ...                                   630
96      Continente, subcontinente o región geográfica  ...  Años para even- tual dupli- ca- ción

[97 rows x 7 columns]
<class 'list'>
7
'''