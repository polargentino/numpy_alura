import pandas as pd

datos_html = pd.read_html('habitantes.html')
habitantes = datos_html[3]
print(habitantes)

#print(datos_html)
print(type(datos_html))
print(len(datos_html))

'''
     N.º País (o territorio dependiente) Población estimada por la ONU para mediados del año  1950  % del total mundial
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

[238 rows x 4 columns]
<class 'list'>
7
'''