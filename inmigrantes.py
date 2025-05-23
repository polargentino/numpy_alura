import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('inmigrantes_canada.csv')
print(df.head())

print(df.shape)
print(df.info())

df.set_index('Pais',inplace=True)
print(df)

años = list(map(str,range(1980,2014)))
print(años)

colombia = df.loc['Colombia',años]
print(colombia)

col_dict = {'Año':colombia.index.tolist(),
            'Inmigrantes':colombia.values.tolist()}

datos_col = pd.DataFrame(col_dict)
print(datos_col.tail())

plt.figure(figsize=(8,4))
plt.plot(datos_col['Año'],datos_col['Inmigrantes'])
plt.xticks(['1980','1985','1990','1995','2000','2005','2010'])
plt.show()

plt.figure(figsize=(8,4))
plt.plot(datos_col['Año'],datos_col['Inmigrantes'])
plt.xticks(['1980','1985','1990','1995','2000','2005','2010'])
plt.title('Inmigrantes de Colombia hacia Canadá')
plt.xlabel('Año')
plt.ylabel('Inmigrantes')
plt.show()

df_comparacion = df.loc[['Brasil', 'Argentina'], años]
df_comparacion = df_comparacion.T
print(df_comparacion.head())

plt.plot(df_comparacion['Brasil'], label='Brasil')
plt.plot(df_comparacion['Argentina'], label='Argentina')
plt.title('Inmigración de Brasil y Argentina a Canadá')
plt.xlabel('Año')
plt.ylabel('Número de Inmigrantes')
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010'])
plt.legend()
plt.show()

fig, ax = plt.subplots(figsize=(8,4))
ax.plot(datos_col['Año'],datos_col['Inmigrantes'])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.set_title('Inmigrantes de Colombia hacia Canadá\n1980 - 2013\nPor Pol Monsalvo')
ax.set_xlabel('Año')
ax.set_ylabel('Número de Inmigrantes')
plt.show()

import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2, figsize=(10, 3))

axs[0].plot(datos_col['Año'], datos_col['Inmigrantes'])
axs[0].set_title('Inmigrantes de Colombia hacia Canadá\n1980 - 2013')
axs[0].set_xlabel('Año')
axs[0].set_ylabel('Número de Inmigrantes')
axs[0].xaxis.set_major_locator(plt.MultipleLocator(5))
axs[0].grid()

axs[1].boxplot(datos_col['Inmigrantes'])
axs[1].set_title('Distribución de Inmigrantes de Colombia\nhacia Canadá 1980 - 2013')

axs[1].set_xlabel('Colombia')
axs[1].set_ylabel('Número de Inmigrantes')
axs[1].grid()

plt.show()


fig, axs = plt.subplots(2, 2, figsize=(10, 6))
fig.subplots_adjust(hspace=0.5, wspace=0.3)

axs[0,0].plot(df.loc['Colombia', años])
axs[0,0].set_title('Colombia')

axs[0,1].plot(df.loc['Brasil', años])
axs[0,1].set_title('Brasil')

axs[1,0].plot(df.loc['Argentina', años])
axs[1,0].set_title('Argentina')

axs[1,1].plot(df.loc['Perú', años])
axs[1,1].set_title('Perú')

for ax in axs.flat:
    ax.xaxis.set_major_locator(plt.MultipleLocator(5))
    
    ax.set_xlabel=('Año')
    ax.set_ylabel=('Número de Inmigrantes')

plt.show()

fig, axs = plt.subplots(2, 2, figsize=(10, 6))
fig.subplots_adjust(hspace=0.5, wspace=0.3)
fig.suptitle('Inmigración de los 4 mayores países sudamericanos\nhacia Canadá desde 1980 - 2013')

axs[0,0].plot(df.loc['Colombia', años])
axs[0,0].set_title('Colombia')

axs[0,1].plot(df.loc['Brasil', años])
axs[0,1].set_title('Brasil')

axs[1,0].plot(df.loc['Argentina', años])
axs[1,0].set_title('Argentina')

axs[1,1].plot(df.loc['Perú', años])
axs[1,1].set_title('Perú')

ymin = 0
ymax = 7000
for ax in axs.ravel():
    ax.set_ylim(ymin, ymax)

for ax in axs.flat:
    ax.xaxis.set_major_locator(plt.MultipleLocator(5))
    
    ax.set_xlabel=('Año')
    ax.set_ylabel=('Número de Inmigrantes')
    ax.grid()

plt.show()

# Desafío: visualizando datos de ventas de tiendas diferentes
tiendas = ['A', 'B', 'C', 'D']
ventas_2022 = {'Ene': [100, 80, 150, 50],
    'Feb': [120, 90, 170, 60],
    'Mar': [150, 100, 200, 80],
    'Abr': [180, 110, 230, 90],
    'May': [220, 190, 350, 200],
    'Jun': [230, 150, 280, 120],
    'Jul': [250, 170, 300, 140],
    'Ago': [260, 180, 310, 150],
    'Sep': [240, 160, 290, 130],
    'Oct': [220, 140, 270, 110],
    'Nov': [400, 220, 350, 190],
    'Dec': [300, 350, 400, 250]}

df = pd.DataFrame(ventas_2022, index=tiendas)
print(df.tail())

# Crear la figura y los subgráficos

fig, axs = plt.subplots(2, 2, figsize=(14, 8))

# Ajustar los espaciados entre los subgráficos

plt.subplots_adjust(wspace=0.3, hspace=0.4)

# Agregar un título general para los subgráficos

fig.suptitle('Ventas en el período de enero a diciembre de 2022 en las tiendas A, B, C y D')

# Agregar los gráficos en cada uno de los subgráficos

axs[0, 0].plot(df.loc['A'])
axs[0, 0].set_title('Ventas en la tienda A')
axs[0, 1].plot(df.loc['B'])
axs[0, 1].set_title('Ventas en la tienda B')
axs[1, 0].plot(df.loc['C'])
axs[1, 0].set_title('Ventas en la tienda C')
axs[1, 1].plot(df.loc['D'])
axs[1, 1].set_title('Ventas en la tienda D')

# Agregar etiquetas para los ejes X y Y

for ax in axs.flat:
    ax.set_xlabel('Mes')
    ax.set_ylabel('Número de ventas')
    ax.grid()
# Mostrar la figura

plt.show()

fig, ax = plt.subplots(figsize=(8,3))
ax.plot(datos_col['Año'],datos_col['Inmigrantes'], lw=2, marker='o')
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.set_title('Inmigrantes de Colombia hacia Canadá\n1980 - 2013\nPor Pol Monsalvo con Alura Latam', fontsize=18, loc='left')
ax.set_xlabel('Año', fontsize=14)
ax.set_ylabel('Número de Inmigrantes', fontsize=14)
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)
ax.grid()
plt.show()

print(plt.style.available)

'''
              Pais Continente           Region  1980  1981  1982  ...  2009  2010  2011  2012  2013  Total
0       Afganistán       Asia      Sur de Asia    16    39    39  ...  1746  1758  2203  2635  2004  58639
1          Albania     Europa    Sur de Europa     1     0     0  ...   716   561   539   620   603  15699
2          Argelia     África  Norte de África    80    67    71  ...  5393  4752  4325  3774  4331  69439
3  Samoa Americana    Oceanía        Polinesia     0     1     0  ...     0     0     0     0     0      6
4          Andorra     Europa    Sur de Europa     0     0     0  ...     0     0     0     1     1     15

[5 rows x 38 columns]
(195, 38)
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 195 entries, 0 to 194
Data columns (total 38 columns):
 #   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   Pais        195 non-null    object
 1   Continente  195 non-null    object
 2   Region      195 non-null    object
 3   1980        195 non-null    int64 
 4   1981        195 non-null    int64 
 5   1982        195 non-null    int64 
 6   1983        195 non-null    int64 
 7   1984        195 non-null    int64 
 8   1985        195 non-null    int64 
 9   1986        195 non-null    int64 
 10  1987        195 non-null    int64 
 11  1988        195 non-null    int64 
 12  1989        195 non-null    int64 
 13  1990        195 non-null    int64 
 14  1991        195 non-null    int64 
 15  1992        195 non-null    int64 
 16  1993        195 non-null    int64 
 17  1994        195 non-null    int64 
 18  1995        195 non-null    int64 
 19  1996        195 non-null    int64 
 20  1997        195 non-null    int64 
 21  1998        195 non-null    int64 
 22  1999        195 non-null    int64 
 23  2000        195 non-null    int64 
 24  2001        195 non-null    int64 
 25  2002        195 non-null    int64 
 26  2003        195 non-null    int64 
 27  2004        195 non-null    int64 
 28  2005        195 non-null    int64 
 29  2006        195 non-null    int64 
 30  2007        195 non-null    int64 
 31  2008        195 non-null    int64 
 32  2009        195 non-null    int64 
 33  2010        195 non-null    int64 
 34  2011        195 non-null    int64 
 35  2012        195 non-null    int64 
 36  2013        195 non-null    int64 
 37  Total       195 non-null    int64 
dtypes: int64(35), object(3)
memory usage: 58.0+ KB
None
                  Continente            Region  1980  1981  1982  1983  ...  2009  2010  2011  2012  2013  Total
Pais                                                                    ...                                     
Afganistán              Asia       Sur de Asia    16    39    39    47  ...  1746  1758  2203  2635  2004  58639
Albania               Europa     Sur de Europa     1     0     0     0  ...   716   561   539   620   603  15699
Argelia               África   Norte de África    80    67    71    69  ...  5393  4752  4325  3774  4331  69439
Samoa Americana      Oceanía         Polinesia     0     1     0     0  ...     0     0     0     0     0      6
Andorra               Europa     Sur de Europa     0     0     0     0  ...     0     0     0     1     1     15
...                      ...               ...   ...   ...   ...   ...  ...   ...   ...   ...   ...   ...    ...
Vietnam                 Asia  Sudeste Asiático  1191  1829  2162  3404  ...  2171  1942  1723  1731  2112  97146
Sahara Occidental     África   Norte de África     0     0     0     0  ...     0     0     0     0     0      2
Yemen                   Asia   Asia Occidental     1     2     1     6  ...   128   211   160   174   217   2985
Zambia                África   África Oriental    11    17    11     7  ...    60   102    69    46    59   1677
Zimbabue              África   África Oriental    72   114   102    44  ...   508   494   434   437   407   8598

[195 rows x 37 columns]
['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013']
1980     266
1981     326
1982     360
1983     244
1984     235
1985     214
1986     257
1987     376
1988     352
1989     439
1990     614
1991     652
1992     582
1993     464
1994     375
1995     371
1996     381
1997     578
1998     929
1999    1306
2000    2259
2001    2965
2002    3283
2003    4318
2004    4566
2005    6424
2006    6535
2007    5357
2008    5452
2009    4652
2010    5218
2011    4366
2012    3741
2013    3631
Name: Colombia, dtype: object
     Año  Inmigrantes
29  2009         4652
30  2010         5218
31  2011         4366
32  2012         3741
33  2013         3631
Pais  Brasil  Argentina
1980     211        368
1981     220        426
1982     192        626
1983     139        241
1984     145        237
   Ene  Feb  Mar  Abr  May  Jun  Jul  Ago  Sep  Oct  Nov  Dec
A  100  120  150  180  220  230  250  260  240  220  400  300
B   80   90  100  110  190  150  170  180  160  140  220  350
C  150  170  200  230  350  280  300  310  290  270  350  400
D   50   60   80   90  200  120  140  150  130  110  190  250
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'petroff10', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']
'''
