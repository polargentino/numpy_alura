'''
Ir a: https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Movies y guardar el archivo .html, 
renombrarlo: movies_wiki.html y ejecutar el código: 

Nos intereresa el segundo [1] lo desarrollamos en el sig. archivo: ller_html_1.py
'''

import pandas as pd

datos_html = pd.read_html('movies_wiki.html')
print(datos_html)
print(type(datos_html))
print(len(datos_html))

'''
[       0                      1
0   1998             100 Movies
1   1999              100 Stars
2   2000             100 Laughs
3   2001            100 Thrills
4   2002           100 Passions
5   2003  100 Heroes & Villains
6   2004              100 Songs
7   2005       100 Movie Quotes
8   2005              25 Scores
9   2006             100 Cheers
10  2006            25 Musicals
11  2007   100 Movies (Updated)
12  2008        AFI's 10 Top 10
13   vte                    vte,                       Film  Release year  ... 1998 Rank 2007 Rank
0             Citizen Kane          1941  ...         1         1
1               Casablanca          1942  ...         2         3
2            The Godfather          1972  ...         3         2
3       Gone with the Wind          1939  ...         4         6
4       Lawrence of Arabia          1962  ...         5         7
..                     ...           ...  ...       ...       ...
118        Sophie's Choice          1982  ...         -        91
119  The Last Picture Show          1971  ...         -        95
120     Do the Right Thing          1989  ...         -        96
121           Blade Runner          1982  ...         -        97
122              Toy Story          1995  ...         -        99

[123 rows x 6 columns]]
<class 'list'>
2
'''