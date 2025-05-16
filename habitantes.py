import pandas as pd

datos_html = pd.read_html('habitantes.html')
print(datos_html)
print(type(datos_html))
print(len(datos_html))

'''
[     N.º  ... Enlace o hipervínculo (usualmente de tipo oficial) de esta última cifra de población
0      1  ...                                    web.archive.org                                  
1      2  ...                                   www.stats.gov.cn                                  
2      3  ...                                     www.census.gov                                  
3      4  ...                  dispendukcapil.acehtimurkab.go.id                                  
4      5  ...                                     www.pbs.gov.pk                                  
..   ...  ...                                                ...                                  
241  242  ...                              www.citypopulation.de                                  
242  243  ...                                   www.statoids.com                                  
243  244  ...                                 www.immigration.pn                                  
244  NaN  ...                              www.worldometers.info                                  
245   N°  ...  Enlace o hipervínculo (usualmente de tipo ofic...                                  

[246 rows x 12 columns],         Continente, subcontinente o región geográfica  ...  Años para even- tual dupli- ca- ción
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

[97 rows x 7 columns],                                                    N.º  ...  % del total mundial
                                                   N.º  ...  % del total mundial
                                                   N.º  ...  % del total mundial
0    Tabla de países y territorios dependientes por...  ...                  NaN
1    N.º País (o territorio dependiente) Población ...  ...                  NaN
2                                                  N.º  ...  % del total mundial
3                                                    1  ...                 2177
4                                                    2  ...                 1428
..                                                 ...  ...                  ...
714                                                234  ...                  000
715                                                235  ...                  000
716                                                236  ...                  000
717                                                237  ...                  000
718                                                  -  ...                10000

[719 rows x 4 columns],      N.º País (o territorio dependiente) Población estimada por la ONU para mediados del año  1950  % del total mundial
0      1                           China                                        543 979 000                        2177
1      2                           India                                        357 021 000                        1428
2      3                  Estados Unidos                                        148 282 000                         593
3      4                           Rusia                                        102 580 000                         410
4      5                           Japón                                         84 353 000                         338
..   ...                             ...                                                ...                         ...
233  234         San Bartolomé (Francia)                                              2 000                           0
234  235                    Tokelau (NZ)                                              2 000                           0
235  236             Ciudad del Vaticano                                              1 000                           0
236  237                 San Martín (PB)                                              1 000                           0
237    -                           Mundo                                  2 499 327 000 000                       10000

[238 rows x 4 columns],      N.º País (o territorio dependiente) Población estimada por la ONU para mediados del año  1975  % del total mundial
0      1                           China                                        915 125 000                        2249
1      2                           India                                        623 524 000                        1532
2      3                  Estados Unidos                                        211 275 000                         519
3      4                           Rusia                                        133 842 000                         329
4      5                       Indonesia                                        131 213 000                         322
..   ...                             ...                                                ...                         ...
233  234         San Bartolomé (Francia)                                              3 000                           0
234  235             Islas Malvinas (RU)                                              2 000                           0
235  236                    Tokelau (NZ)                                              2 000                           0
236  237             Ciudad del Vaticano                                              1 000                           0
237    -                           Mundo                                  4 069 441 000 000                       10000

[238 rows x 4 columns],      N.º País (o territorio dependiente) Población estimada por la ONU para mediados del año  2000  % del total mundial
0      1                           China                                      1 264 099 000                        2056
1      2                           India                                      1 059 634 000                        1723
2      3                  Estados Unidos                                        282 399 000                         459
3      4                       Indonesia                                        214 072 000                         348
4      5                          Brasil                                        175 874 000                         286
..   ...                             ...                                                ...                         ...
233  234             Islas Malvinas (RU)                                              3 000                           0
234  235                       Niue (NZ)                                              2 000                           0
235  236                    Tokelau (NZ)                                              2 000                           0
236  237             Ciudad del Vaticano                                              1 000                           0
237    -                           Mundo                                  6 148 898 000 000                       10000

[238 rows x 4 columns],                         0                                    1
0  Control de autoridades  Proyectos Wikimedia  Datos: Q712280]
<class 'list'>
7
'''