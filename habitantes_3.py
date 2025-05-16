import pandas as pd

datos_html = pd.read_html('habitantes.html')
habitantes = datos_html[2]
print(habitantes)

#print(datos_html)
print(type(datos_html))
print(len(datos_html))
'''
                                                   N.º  ...  % del total mundial
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

[719 rows x 4 columns]
<class 'list'>
7
'''