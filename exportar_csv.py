import pandas as pd

datos_html = pd.read_html('movies_wiki.html')
top_peliculas = datos_html[1]

top_peliculas.to_csv('top_peliculas_1998.csv', index=False)

datos = pd.read_csv('top_peliculas_1998.csv')

print(datos.head())

'''
                 Film  Release year              Director                    Production companies 1998 Rank 2007 Rank
0        Citizen Kane          1941          Orson Welles                      RKO Radio Pictures         1         1
1          Casablanca          1942        Michael Curtiz                   Warner Bros. Pictures         2         3
2       The Godfather          1972  Francis Ford Coppola  Paramount Pictures, Alfran Productions         3         2
3  Gone with the Wind          1939        Victor Fleming         Selznick International Pictures         4         6
4  Lawrence of Arabia          1962            David Lean                        Horizon Pictures         5         7



Film,Release year,Director,Production companies,1998 Rank,2007 Rank
Citizen Kane,1941,Orson Welles,RKO Radio Pictures,1,1
Casablanca,1942,Michael Curtiz,Warner Bros. Pictures,2,3
The Godfather,1972,Francis Ford Coppola,"Paramount Pictures, Alfran Productions",3,2
Gone with the Wind,1939,Victor Fleming,Selznick International Pictures,4,6
Lawrence of Arabia,1962,David Lean,Horizon Pictures,5,7
The Wizard of Oz,1939,Victor Fleming,Metro-Goldwyn-Mayer,6,10
The Graduate,1967,Mike Nichols,Lawrence Turman,7,17
'''