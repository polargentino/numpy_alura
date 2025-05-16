import pandas as pd
import matplotlib.pyplot as plt
import mpld3

def analizar_datos_poblacion(archivo_html, archivo_salida):
    """
    Analiza y visualiza datos de población obtenidos de un archivo HTML y guarda los gráficos en un archivo HTML.

    Esta función lee un archivo HTML que contiene datos de población, los normaliza,
    realiza análisis y visualizaciones para mostrar los países con mayor población
    y los países con mayor porcentaje del total mundial, y guarda los gráficos en un archivo HTML.

    Parámetros:
    -----------
    archivo_html : str
        Ruta al archivo HTML que contiene los datos de población.
    archivo_salida : str
        Ruta al archivo HTML donde se guardarán los gráficos.

    Retorna:
    --------
    None
    """
    # Leer las tablas del archivo HTML
    datos_html = pd.read_html(archivo_html)

    # Seleccionar la tabla específica (índice 5 en este caso)
    habitantes = datos_html[5]

    # Renombrar las columnas para facilitar el acceso a los datos
    habitantes.columns = ['N.º', 'País', 'Población', '% del total mundial']

    # Limpiar y convertir la columna 'Población' a tipo entero
    habitantes['Población'] = habitantes['Población'].str.replace('\xa0', '').str.replace(' ', '').astype(int)

    # Crear figuras para los gráficos
    fig1, ax1 = plt.subplots(figsize=(12, 8))
    fig2, ax2 = plt.subplots(figsize=(12, 8))

    # Visualización de los 10 países con mayor población
    habitantes_ordenados = habitantes.sort_values(by='Población', ascending=False)
    top_10_paises = habitantes_ordenados.head(10)

    ax1.bar(top_10_paises['País'], top_10_paises['Población'])
    ax1.set_xlabel('País')
    ax1.set_ylabel('Población')
    ax1.set_title('Top 10 Países por Población')
    ax1.tick_params(axis='x', rotation=45)

    # Visualización de los 10 países con mayor porcentaje del total mundial
    habitantes_porcentaje = habitantes.sort_values(by='% del total mundial', ascending=False)
    top_10_porcentaje = habitantes_porcentaje.head(10)

    ax2.bar(top_10_porcentaje['País'], top_10_porcentaje['% del total mundial'])
    ax2.set_xlabel('País')
    ax2.set_ylabel('% del Total Mundial')
    ax2.set_title('Top 10 Países por % del Total Mundial')
    ax2.tick_params(axis='x', rotation=45)

    # Guardar los gráficos en un archivo HTML
    with open(archivo_salida, 'w') as f:
        f.write(mpld3.fig_to_html(fig1))
        f.write(mpld3.fig_to_html(fig2))

# Ejemplo de uso
analizar_datos_poblacion('habitantes.html', 'graficos_poblacion.html')

'''
Explicación del Código:
Importar mpld3:

import mpld3: Importa la biblioteca mpld3 para convertir los gráficos en formato HTML.
Crear figuras para los gráficos:

fig1, ax1 = plt.subplots(figsize=(12, 8)): Crea una figura y un eje para el primer gráfico.
fig2, ax2 = plt.subplots(figsize=(12, 8)): Crea una figura y un eje para el segundo gráfico.
Guardar los gráficos en un archivo HTML:

mpld3.fig_to_html(fig1): Convierte la figura del primer gráfico a formato HTML.
mpld3.fig_to_html(fig2): Convierte la figura del segundo gráfico a formato HTML.
with open(archivo_salida, 'w') as f:: Abre un archivo HTML en modo escritura y guarda los gráficos en él.

Explicación de los Cambios:
Uso de tick_params:

ax1.tick_params(axis='x', rotation=45): Utiliza tick_params para rotar las etiquetas del eje x, lo cual es más adecuado para evitar las advertencias.
Advertencias de Deprecación:

Las advertencias de deprecación relacionadas con matplotlib son internas de la biblioteca mpld3 y no afectan directamente el código. Estas advertencias son informativas y no deberían afectar la funcionalidad de tu código.
'''
