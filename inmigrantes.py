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

