import pandas as pd

datos_html = pd.read_html('habitantes.html')
habitantes = datos_html[6]
print(habitantes)

#print(datos_html)
print(type(datos_html))
print(len(datos_html))

'''
                        0                                    1
0  Control de autoridades  Proyectos Wikimedia  Datos: Q712280
<class 'list'>
7
'''
