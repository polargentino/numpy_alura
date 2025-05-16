import pandas as pd

datos_html = pd.read_html('habitantes.html')
habitantes = datos_html[5]
print(habitantes)

#print(datos_html)
print(type(datos_html))
print(len(datos_html))

'''
     N.º País (o territorio dependiente) Población estimada por la ONU para mediados del año  2000  % del total mundial
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

[238 rows x 4 columns]
<class 'list'>
7
'''