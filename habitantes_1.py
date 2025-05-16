import pandas as pd

datos_html = pd.read_html('habitantes.html')
habitantes = datos_html[0]
print(habitantes)

#print(datos_html)
print(type(datos_html))
print(len(datos_html))
'''
     N.º  ... Enlace o hipervínculo (usualmente de tipo oficial) de esta última cifra de población
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

[246 rows x 12 columns]
<class 'list'>
7
   
'''