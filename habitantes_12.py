import pandas as pd

# Leer las tablas del archivo HTML
datos_html = pd.read_html('habitantes.html')

# Seleccionar la tabla específica (índice 5 en este caso)
habitantes = datos_html[5]

# Renombrar las columnas para facilitar el acceso a los datos
habitantes.columns = ['N.º', 'País', 'Población', '% del total mundial']

# Limpiar y convertir la columna 'Población' a tipo entero
habitantes['Población'] = habitantes['Población'].str.replace('\xa0', '').str.replace(' ', '').astype(int)

# Exportar la tabla a un archivo HTML
habitantes.to_html('tabla_poblacion.html', index=False)

print("Tabla exportada a 'tabla_poblacion.html'")

'''
Tabla exportada a 'tabla_poblacion.html'
'''