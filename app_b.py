# -*- coding: utf-8 -*-
"""
Script para cargar datos de manzanas desde un archivo CSV local con nombres de ciudades,
separar nombres de ciudades y datos numéricos usando indexación de structured array,
y graficar cada serie de datos por ciudad.
"""

# Importar las bibliotecas necesarias
import numpy as np             # Para manejo de arrays y funciones numéricas
import matplotlib.pyplot as plt # Para crear y mostrar gráficos

# --- Configuración ---
# Ruta al archivo CSV en tu sistema. Asegúrate de que esta ruta sea correcta.
archivo_csv = "/home/pol/Descargas/manzanas.csv"

# --- Carga de Datos ---
# El bloque try principal para manejar errores generales, como FileNotFoundError
try:
    # Usamos np.genfromtxt porque puede manejar diferentes tipos de datos
    # (strings para nombres, números para valores) y valores faltantes (NaN).
    # delimiter=',': Especifica que las columnas están separadas por comas.
    # skip_header=1: Omite la primera fila, que contiene las etiquetas de tiempo/fecha.
    # dtype=None: Permite a NumPy inferir el tipo de datos de cada columna automáticamente.
    # encoding='utf-8': Especifica la codificación del archivo para manejar caracteres especiales si los hay.
    # Con dtype=None y columnas mixtas, genfromtxt a menudo carga un array 1D de estructuras.
    data = np.genfromtxt(archivo_csv, delimiter=",", skip_header=1, dtype=None, encoding='utf-8')

    print(f"Archivo '{archivo_csv}' cargado correctamente.")
    print("Forma de los datos cargados:", np.shape(data))
    # Si la forma es (5,), np.genfromtxt probablemente cargó un array 1D de estructuras.

    # --- Separar Nombres de Ciudades y Datos Numéricos ---
    # Si data es un array 1D de estructuras, accedemos a los campos por su nombre asignado ('f0', 'f1', etc.)
    # 'f0' es típicamente el nombre del primer campo/columna.
    nombres_ciudades = data['f0']

    # --- Obtener Etiquetas de Fechas del Encabezado ---
    # Leemos el encabezado por separado para obtener las etiquetas de los meses/años.
    try: # Try anidado para manejar errores solo al leer el encabezado
        with open(archivo_csv, 'r', encoding='utf-8') as f:
            # Lee la primera línea del archivo
            header_line = f.readline().strip()
            # Divide la línea por comas para obtener la lista de etiquetas
            fechas = header_line.split(',')

        # Las etiquetas de las fechas útiles comienzan desde la segunda columna del encabezado (índice 1).
        # La primera columna del encabezado a menudo está vacía o es una etiqueta genérica.
        fechas_labels = fechas[1:]

        # --- Preparar Datos Numéricos para Graficar ---
        # Las columnas numéricas serán 'f1', 'f2', ..., hasta el final.
        # Necesitamos obtener los nombres de estos campos numéricos dinámicamente del structured array.
        # data.dtype.names es una tupla con los nombres de todos los campos ('f0', 'f1', 'f2', ...).
        campos_numericos_nombres = data.dtype.names[1:] # Nombres de los campos excluyendo 'f0'

        # Verificar que la cantidad de etiquetas de fechas coincida con la cantidad de campos numéricos detectados.
        num_columnas_numericas_detectadas = len(campos_numericos_nombres)
        num_columnas_reales_en_header = len(fechas_labels)


        if num_columnas_reales_en_header != num_columnas_numericas_detectadas:
             print(f"Advertencia: El número de etiquetas de fecha en el encabezado ({num_columnas_reales_en_header}) no coincide con el número de campos numéricos detectados por genfromtxt ({num_columnas_numericas_detectadas}).")
             # Si no coinciden, usamos los nombres de campo detectados como etiquetas genéricas para el eje X.
             fechas_labels = campos_numericos_nombres # Usar 'f1', 'f2', etc. como etiquetas
             print("Usando nombres de campo detectados como etiquetas de eje X.")

        # Extraemos los datos de cada campo numérico y los apilamos como columnas para formar un array 2D numérico.
        # [data[nombre_campo].reshape(-1, 1) for nombre_campo in campos_numericos_nombres] crea una lista
        # donde cada elemento es un array columna (forma (5, 1)) para cada campo numérico ('f1', 'f2', etc.).
        # np.hstack apila estos arrays columna horizontalmente para crear el array 2D final.
        # El resultado tendrá forma (num_filas, num_campos_numericos) => (5, 90)
        datos_numericos = np.hstack([data[nombre_campo].reshape(-1, 1) for nombre_campo in campos_numericos_nombres])

        print(f"Se extrajeron {len(nombres_ciudades)} ciudades.")
        print(f"Los datos numéricos para graficar tienen forma {datos_numericos.shape}.")


        # --- Graficar Datos por Ciudad ---

        print("Generando gráficos para cada ciudad...")

        # Iterar sobre cada fila del array de datos numéricos
        # 'i' es el índice de la fila (0 para Moscu, 1 para Kaliningrado, etc.)
        # 'valores_ciudad' es el array 1D con los datos de esa ciudad a lo largo del tiempo
        # Usamos enumerate para obtener tanto el índice como los valores de la fila
        for i, valores_ciudad in enumerate(datos_numericos):
            # Obtener el nombre de la ciudad correspondiente usando el mismo índice 'i'
            nombre_ciudad = nombres_ciudades[i]

            # Crear una nueva figura para cada gráfico, así se muestran por separado
            # figsize define el tamaño de la ventana del gráfico (ancho, alto en pulgadas)
            plt.figure(figsize=(12, 6))

            # Graficar los valores de la ciudad contra las etiquetas de fecha/tiempo
            # plt.plot ignora automáticamente los valores np.nan (Not a Number)
            plt.plot(fechas_labels, valores_ciudad, marker='o', linestyle='-') # marker y linestyle son opcionales

            # Añadir títulos y etiquetas al gráfico actual
            plt.title(f'Datos (Manzanas?) en {nombre_ciudad}') # Título descriptivo
            plt.xlabel('Fecha')        # Etiqueta del eje X
            plt.ylabel('Valor')       # Etiqueta del eje Y (ajústala según el significado de los datos)
            plt.grid(True)             # Mostrar cuadrícula

            # Rotar etiquetas del eje X si son largas (como fechas) y ajustar layout para evitar superposición
            # Solo aplicamos rotación y tight_layout si usamos las fechas reales como etiquetas
            if num_columnas_reales_en_header == num_columnas_numericas_detectadas:
                 plt.xticks(rotation=45, ha='right') # rota 45 grados, alinea a la derecha del tick
                 plt.tight_layout() # Ajusta automáticamente el espacio para evitar recortes

            # Mostrar el gráfico de la ciudad actual.
            # El script pausará aquí hasta que cierres la ventana del gráfico.
            plt.show()

        print("\nGeneración de gráficos completada.")

    # Este except maneja errores específicamente al leer el encabezado dentro del try anidado
    # No necesitamos re-lanzar la excepción porque ya manejamos el caso con etiquetas genéricas.
    except Exception as e_header:
         print(f"Ocurrió un error al leer el encabezado del archivo CSV: {e_header}")
         # Como alternativa, aquí podrías decidir salir o usar otro manejo.
         # El código continuará usando etiquetas genéricas si esto falla.


# Este except maneja el caso específico de que el archivo no exista
# Debe estar al mismo nivel de indentación que el primer 'try:'
except FileNotFoundError:
    print(f"Error: El archivo CSV no fue encontrado en la ruta especificada: {archivo_csv}")
    print("Por favor, verifica la ruta y el nombre del archivo.")

# Este except captura cualquier otro error general que no haya sido manejado específicamente
# Debe estar al mismo nivel de indentación que el primer 'try:'
except Exception as e:
    print(f"Ocurrió un error inesperado durante la carga o graficación: {e}")