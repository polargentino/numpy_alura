import pandas as pd
import plotly.express as px

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

    # Crear gráficos con Plotly
    fig1 = px.bar(habitantes.sort_values(by='Población', ascending=False).head(10),
                 x='País', y='Población',
                 title='Top 10 Países por Población',
                 labels={'País': 'País', 'Población': 'Población'})

    fig2 = px.bar(habitantes.sort_values(by='% del total mundial', ascending=False).head(10),
                 x='País', y='% del total mundial',
                 title='Top 10 Países por % del Total Mundial',
                 labels={'País': 'País', '% del total mundial': '% del Total Mundial'})

    # Guardar los gráficos en un archivo HTML
    fig1.write_html(archivo_salida)
    fig2.write_html(archivo_salida.replace('.html', '_porcentaje.html'))

# Ejemplo de uso
analizar_datos_poblacion('habitantes.html', 'graficos_poblacion.html')

'''
Explicación del Código:
Importar plotly.express:

import plotly.express as px: Importa la biblioteca plotly.express para crear gráficos interactivos.
Crear gráficos con Plotly:

fig1 = px.bar(...): Crea un gráfico de barras para los 10 países con mayor población.
fig2 = px.bar(...): Crea un gráfico de barras para los 10 países con mayor porcentaje del total mundial.
Guardar los gráficos en un archivo HTML:

fig1.write_html(archivo_salida): Guarda el primer gráfico en un archivo HTML.
fig2.write_html(archivo_salida.replace('.html', '_porcentaje.html')): Guarda el segundo gráfico en otro archivo HTML.
Este código te permitirá crear gráficos interactivos y guardarlos en archivos HTML sin las advertencias de deprecación. Si tienes más preguntas o necesitas más ayuda, no dudes en decírmelo.
'''