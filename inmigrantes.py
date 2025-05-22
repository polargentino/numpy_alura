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

