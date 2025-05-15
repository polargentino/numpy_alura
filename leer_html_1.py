import pandas as pd

datos_html = pd.read_html('movies_wiki.html')
top_peliculas = datos_html[1]
print(top_peliculas)
'''
                      Film  Release year  ... 1998 Rank 2007 Rank
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

[123 rows x 6 columns]
'''