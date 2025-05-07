import numpy as np

# URL correcta del archivo CSV
url = 'https://gist.githubusercontent.com/ahcamachod/9be09de793dc3bf1e6c3d98eb4e5b1ef/raw/21b85572693200040e11284ef6dcfc3457ec8e11/citrus.csv'

try:
    # Cargar datos numéricos (columnas 1 a 5: diametro, peso, rojo, verde, azul)
    datos = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 6, 1), skiprows=1)
    print("Datos cargados correctamente. Forma:", np.shape(datos))

    # ====== Ejemplos de funciones NumPy con 'datos' ======

    # 1. Calcular estadísticas básicas (Media, Desviación Estándar, Mínimo, Máximo)
    # Puedes aplicar funciones a todo el array, o a lo largo de un eje específico (filas o columnas).
    # axis=0 significa aplicar la función por columna.
    # axis=1 significa aplicar la función por fila (menos común en este caso).

    print("\nEstadísticas por columna (axis=0):")
    # Recordar que las columnas son [diametro, peso, rojo, verde, azul]
    media_por_columna = np.mean(datos, axis=0)
    print(f"Media por columna: {media_por_columna}")

    std_por_columna = np.std(datos, axis=0)
    print(f"Desviación Estándar por columna: {std_por_columna}")

    min_por_columna = np.min(datos, axis=0)
    print(f"Mínimo por columna: {min_por_columna}")

    max_por_columna = np.max(datos, axis=0)
    print(f"Máximo por columna: {max_por_columna}")

    # También puedes obtener estadísticas de una columna específica.
    # Por ejemplo, la columna del peso es la columna 1 (índice 1, ya que empezamos en 0 para el array cargado)
    peso_columna = datos[:, 1] # Selecciona todas las filas (:) de la columna con índice 1
    media_peso = np.mean(peso_columna)
    print(f"\nMedia específica del Peso: {media_peso}")

    # 2. Filtrar o seleccionar datos basados en condiciones
    # Por ejemplo, seleccionar todas las filas donde el diámetro (columna 0 en el array) sea mayor a 8.0
    diametro = datos[:, 0] # Columna del diámetro
    condicion_diametro_grande = diametro > 8.0
    datos_diametro_grande = datos[condicion_diametro_grande] # Usar la condición para indexar el array

    print(f"\nCantidad de frutas con diámetro > 8.0: {len(datos_diametro_grande)}")
    # print("Primeras 5 filas de frutas con diámetro > 8.0:")
    # print(datos_diametro_grande[:5])

    # Combinar condiciones (por ejemplo, diámetro > 8.0 Y peso < 250)
    peso = datos[:, 1] # Columna del peso
    condicion_combinada = (diametro > 8.0) & (peso < 250) # '&' para AND lógico en NumPy
    datos_filtrados_combinados = datos[condicion_combinada]
    print(f"Cantidad de frutas con diámetro > 8.0 Y peso < 250: {len(datos_filtrados_combinados)}")


    # 3. Realizar operaciones matemáticas
    # Por ejemplo, crear una nueva "columna" (o un array) que sea la suma de rojo, verde y azul
    suma_colores = datos[:, 2] + datos[:, 3] + datos[:, 4] # Suma elemento por elemento de las columnas
    print(f"\nPrimeros 5 valores de la suma de colores: {suma_colores[:5]}")

    # Puedes añadir esta 'columna' si fuera necesario (aunque no siempre es la mejor práctica para datos mixtos)
    # datos_con_suma_colores = np.column_stack((datos, suma_colores))
    # print("Forma del array con la columna de suma de colores:", np.shape(datos_con_suma_colores))


    # 4. Ordenar los datos
    # Ordenar el array completo basado en una columna específica, por ejemplo, por peso (columna 1)
    indices_ordenados_por_peso = np.argsort(datos[:, 1]) # Obtiene los índices que ordenarían el array por peso
    datos_ordenados_por_peso = datos[indices_ordenados_por_peso] # Usa los índices para ordenar el array completo

    print("\nPrimeras 5 filas ordenadas por Peso (ascendente):")
    print(datos_ordenados_por_peso[:5])

    # Para ordenar descendente, puedes invertir los índices:
    # datos_ordenados_por_peso_desc = datos[indices_ordenados_por_peso[::-1]]
    # print("\nPrimeras 5 filas ordenadas por Peso (descendente):")
    # print(datos_ordenados_por_peso_desc[:5])


    # 5. Usar broadcasting (operaciones con escalares o arrays de diferente forma)
    # Por ejemplo, sumar 10 a todos los valores de la columna de diámetro
    diametro_ajustado = datos[:, 0] + 10
    print(f"\nPrimeros 5 valores de diámetro ajustado (+10): {diametro_ajustado[:5]}")


except Exception as e:
    print(f"Ocurrió un error: {e}")

'''
Datos cargados correctamente. Forma: (10000, 5)

Estadísticas por columna (axis=0):
Media por columna: [  9.975685 175.050792 153.8478    76.0106    11.3632  ]
Desviación Estándar por columna: [ 1.94774626 29.21065862 10.43243189 11.70784727  9.06082147]
Mínimo por columna: [  2.96  86.76 115.    31.     2.  ]
Máximo por columna: [ 16.45 261.51 192.   116.    56.  ]

Media específica del Peso: 175.050792

Cantidad de frutas con diámetro > 8.0: 8240
Cantidad de frutas con diámetro > 8.0 Y peso < 250: 8228

Primeros 5 valores de la suma de colores: [259. 247. 239. 248. 242.]

Primeras 5 filas ordenadas por Peso (ascendente):
[[  2.96  86.76 172.    85.     2.  ]
 [  3.91  88.05 166.    78.     3.  ]
 [  4.42  95.17 156.    81.     2.  ]
 [  4.47  95.6  163.    81.     4.  ]
 [  4.48  95.76 161.    72.     9.  ]]

Primeros 5 valores de diámetro ajustado (+10): [12.96 13.91 14.42 14.47 14.48]
'''