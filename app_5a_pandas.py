# Importamos la librería pandas, que es fundamental para trabajar con datos en Python.
# La renombramos comúnmente como 'pd' para facilitar su uso.
import pandas as pd

# Definimos la ruta completa o relativa al archivo CSV que queremos leer.
# En este caso, el archivo se llama 'alquiler.csv' y asumimos que está
# en el mismo directorio donde ejecutas este script, o dentro de 'Escritorio/numpy_alura/'.
nombre_archivo = 'alquiler.csv'

# Usamos la función read_csv() de pandas para leer el archivo.
# pandas es muy flexible y puede leer archivos con diferentes formatos.
# El primer argumento es el nombre o la ruta del archivo.
# El argumento 'sep=';'' es crucial aquí. Le decimos a pandas que las columnas
# en tu archivo están separadas por punto y coma (;) en lugar de la coma (,) por defecto.
# El resultado de la lectura se guarda en una estructura de datos de pandas llamada DataFrame,
# que es similar a una tabla de una hoja de cálculo o una base de datos.
datos_alquiler = pd.read_csv(nombre_archivo, sep=';')

# Imprimimos las primeras filas del DataFrame para verificar que se ha leído correctamente.
# El método .head() muestra por defecto las primeras 5 filas.
# Esto nos ayuda a tener una primera vista de los datos y sus columnas.
print(datos_alquiler.head())

# Puedes imprimir todo el DataFrame si es pequeño, pero .head() es mejor para archivos grandes.
# print(datos_alquiler)

'''
Salidas:

                      Tipo           Colonia  Habitaciones  Garages  Suites  Area    Valor  Condominio  Impuesto
0                 Cocineta           Condesa             1        0       0    40   5950.0      1750.0     210.0
1                     Casa           Polanco             2        0       1   100  24500.0         NaN       NaN
2  Conjunto Comercial/Sala          Santa Fe             0        4       0   150  18200.0     14070.0    3888.5
3             Departamento  Centro Histórico             1        0       0    15   2800.0      1365.0      70.0
4             Departamento         Del Valle             1        0       0    48   2800.0       805.0       NaN
                                                                                                                         
¡Genial! 🎉 ¡El código funcionó perfectamente y ya tienes tus datos cargados en un DataFrame de pandas!

Lo que estás viendo en la salida es la representación de las primeras 5 filas de tu archivo alquiler.csv dentro de una estructura de pandas llamada DataFrame.

La primera columna a la izquierda (0, 1, 2, 3, 4) es el índice del DataFrame. Pandas asigna un índice numérico por defecto a cada fila.
La primera fila muestra los nombres de las columnas que leyó del encabezado de tu archivo CSV (Tipo, Colonia, Habitaciones, etc.).
Las celdas contienen los datos de cada fila y columna.
Verás NaN en algunas celdas (por ejemplo, en Condominio e Impuesto para la fila 1 y 4). NaN significa "Not a Number" y pandas lo utiliza para representar valores faltantes o nulos en tus datos. Esto es muy común en conjuntos de datos reales.
Ahora que ya cargamos los datos, un paso fundamental es inspeccionar la estructura y los tipos de datos de nuestro DataFrame. Esto nos ayuda a entender mejor con qué estamos trabajando y a identificar posibles problemas antes de empezar el análisis.

Podemos usar el método .info() del DataFrame para obtener un resumen conciso de su información.

Aquí tienes el código para hacerlo, siguiendo nuestra filosofía de ir paso a paso y con comentarios:
'''