'''
Por Mistral AI, a partir del código anterior que le proporcioné!!
'''

import pandas as pd

# Leer las tablas del archivo HTML
datos_html = pd.read_html('movies_wiki.html')

# Imprimir el número de tablas encontradas
print(f"Número de tablas encontradas: {len(datos_html)}")

# Seleccionar una tabla específica para ver su contenido
# Por ejemplo, seleccionar la segunda tabla (índice 1)
if len(datos_html) > 1:
    top_peliculas = datos_html[1]
    print("\nContenido de la segunda tabla:")
    print(top_peliculas.head())
else:
    print("No hay suficientes tablas en el archivo HTML.")

'''
Número de tablas encontradas: 2

Contenido de la segunda tabla:
                 Film  Release year              Director                    Production companies 1998 Rank 2007 Rank
0        Citizen Kane          1941          Orson Welles                      RKO Radio Pictures         1         1
1          Casablanca          1942        Michael Curtiz                   Warner Bros. Pictures         2         3
2       The Godfather          1972  Francis Ford Coppola  Paramount Pictures, Alfran Productions         3         2
3  Gone with the Wind          1939        Victor Fleming         Selznick International Pictures         4         6
4  Lawrence of Arabia          1962            David Lean                        Horizon Pictures         5         7
'''