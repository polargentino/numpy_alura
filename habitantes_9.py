import pandas as pd
import matplotlib.pyplot as plt

def analizar_datos_poblacion(archivo_html):
    """
    Analiza y visualiza datos de población obtenidos de un archivo HTML.

    Esta función lee un archivo HTML que contiene datos de población, los normaliza,
    y realiza análisis y visualizaciones para mostrar los países con mayor población
    y los países con mayor porcentaje del total mundial.

    Parámetros:
    -----------
    archivo_html : str
        Ruta al archivo HTML que contiene los datos de población.

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

    # Visualización de los 10 países con mayor población
    habitantes_ordenados = habitantes.sort_values(by='Población', ascending=False)
    top_10_paises = habitantes_ordenados.head(10)

    plt.figure(figsize=(10, 5))
    plt.bar(top_10_paises['País'], top_10_paises['Población'])
    plt.xlabel('País')
    plt.ylabel('Población')
    plt.title('Top 10 Países por Población')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Visualización de los 10 países con mayor porcentaje del total mundial
    habitantes_porcentaje = habitantes.sort_values(by='% del total mundial', ascending=False)
    top_10_porcentaje = habitantes_porcentaje.head(10)

    plt.figure(figsize=(10, 5))
    plt.bar(top_10_porcentaje['País'], top_10_porcentaje['% del total mundial'])
    plt.xlabel('País')
    plt.ylabel('% del Total Mundial')
    plt.title('Top 10 Países por % del Total Mundial')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Ejemplo de uso
analizar_datos_poblacion('habitantes.html')
