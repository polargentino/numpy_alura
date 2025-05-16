import pandas as pd

datos_html = pd.read_html('habitantes.html')
habitantes = datos_html[4]
print(habitantes)

#print(datos_html)
print(type(datos_html))
print(len(datos_html))

'''
     N.º País (o territorio dependiente) Población estimada por la ONU para mediados del año  1975  % del total mundial
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

[238 rows x 4 columns]
<class 'list'>
7
'''