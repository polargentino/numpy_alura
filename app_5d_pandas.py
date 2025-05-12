'''
Ahora, para seguir explorando nuestro dataset de forma básica, es útil ver qué tipos de valores 
tenemos en las columnas no numéricas, como Tipo y Colonia. Queremos saber cuántos tipos de inmuebles 
hay y en qué colonias están ubicados.

Para esto, podemos usar dos métodos: .unique() para ver todos los valores distintos, y 
.value_counts() para ver cuántas veces aparece cada valor distinto.

Aquí tienes el código para explorar las columnas Tipo y Colonia, con comentarios:


'''
# Importamos pandas (si no lo has hecho ya)
import pandas as pd

# Cargamos el archivo CSV (si no lo has hecho ya)
nombre_archivo = 'alquiler.csv'
datos_alquiler = pd.read_csv(nombre_archivo, sep=';')

# --- Nuevo Paso: Explorar columnas de texto/categóricas ---

# Seleccionamos la columna 'Tipo'.
# Usamos el método .unique() para obtener un array con todos los valores únicos
# presentes en esa columna. Esto nos muestra la variedad de tipos de inmuebles.
print("\nValores únicos en la columna 'Tipo':")
print(datos_alquiler['Tipo'].unique())

# Usamos el método .value_counts() para contar cuántas veces aparece cada valor único
# en la columna 'Tipo'. Por defecto, ordena los resultados de mayor a menor frecuencia.
# Esto nos dice cuántos inmuebles hay de cada tipo.
print("\nConteo de valores en la columna 'Tipo':")
print(datos_alquiler['Tipo'].value_counts())

# Hacemos lo mismo para la columna 'Colonia'.
print("\nValores únicos en la columna 'Colonia':")
print(datos_alquiler['Colonia'].unique())

# Y contamos cuántos inmuebles hay en cada colonia.
print("\nConteo de valores en la columna 'Colonia':")
print(datos_alquiler['Colonia'].value_counts())

'''

Valores únicos en la columna 'Tipo':
['Cocineta' 'Casa' 'Conjunto Comercial/Sala' 'Departamento'
 'Casa de Condominio' 'Edificio Completo' 'Departamento en Hotel'
 'Tienda/Salón' 'Casa Comercial' 'Casa de Vecindad' 'Terreno Estándar'
 'Cochera/Estacionamiento' 'Loft' 'Galpón/Depósito/Almacén'
 'Tienda en Centro Comercial' 'Rancho' 'Posada/Chalé' 'Estudio' 'Hotel'
 'Loteo/Condominio' 'Industria']

Conteo de valores en la columna 'Tipo':
Tipo
Departamento                  14764
Conjunto Comercial/Sala        5681
Tienda/Salón                   1098
Cocineta                        726
Casa de Condominio              610
Casa                            545
Departamento en Hotel           455
Galpón/Depósito/Almacén         289
Edificio Completo               217
Casa Comercial                  202
Tienda en Centro Comercial      197
Casa de Vecindad                158
Cochera/Estacionamiento          77
Terreno Estándar                 45
Loft                             38
Rancho                            8
Estudio                           4
Loteo/Condominio                  3
Hotel                             2
Posada/Chalé                      1
Industria                         1
Name: count, dtype: int64

Valores únicos en la columna 'Colonia':
['Condesa' 'Polanco' 'Santa Fe' 'Centro Histórico' 'Del Valle' 'Roma'
 'Narvarte' 'Lomas de Chapultepec' 'Coyoacán' 'San Pedro de los Pinos'
 'San Ángel' 'San Jerónimo' 'Ciudad de los Deportes' 'Villa Coapa'
 'Bosques de las Lomas' 'Juárez' 'Chapultepec' 'Lindavista' 'La Condesa'
 'San Miguel Chapultepec' 'Mixcoac' 'El Rosedal' 'Nueva Santa María'
 'Arboledas' 'Villa de Cortés' 'Casa Blanca' 'Bosques de Aragón'
 'La Florida' 'Álvaro Obregón' 'Iztacalco' 'Peralvillo' 'Napoles'
 'Nativitas' 'San Rafael' 'Vallejo' 'Tlalpan' 'Pueblo Culhuacán'
 'San Antonio Tecomitl' 'Roma Norte' 'Industrial Vallejo' 'Iztapalapa'
 'Santa Marta Acatitla' 'Villa de Guadalupe' 'Tláhuac' 'Lomas de Padierna'
 'El Contadero' 'San Mateo' 'Las Águilas' 'Culhuacán CTM'
 'Santa María la Ribera' 'El Arenal' 'San Sebastián' 'Los Alpes'
 'La Merced' 'Barrio Bravo' 'San Andrés Tetepilco' 'Loma Bonita'
 'Tepalcatlalpan' 'Santa Cruz Atoyac' 'El Rodeo' 'La Virgen'
 'San José Insurgentes' 'Atlampa' 'Moctezuma' 'Del Valle Centro'
 'Lindavista Sur' 'Potrero de San Bernardino' 'Santa María Nonoalco'
 'La Loma' 'Doctores' 'Tlalnepantla' 'Historiadores'
 'Residencial Emiliano Zapata' 'San Felipe de Jesús' 'San Juan Xalpa'
 'Zacatenco' 'Roma Sur' 'Santa María Aztahuacán' 'San Gregorio Atlapulco'
 'Reforma Política' 'Los Reyes Coyoacán' 'Atlalilco'
 'Jardines de San Mateo' 'Ajusco' 'Xochimilco' 'Las Aguilas'
 'Santa María Nativitas' 'Pedregal']

Conteo de valores en la columna 'Colonia':
Colonia
Santa Fe                6263
Condesa                 3309
Centro Histórico        3263
Coyoacán                2233
Lomas de Chapultepec    1478
                        ... 
San Mateo                  4
Xochimilco                 4
El Arenal                  2
Las Aguilas                2
Pedregal                   1
Name: count, Length: 88, dtype: int64



Explicación de Gemini: 

¡Excelente! Has explorado exitosamente los valores únicos y sus conteos en las columnas Tipo y Colonia.

Lo que nos muestra este output es:

Valores únicos en la columna 'Tipo':: Vemos la lista completa de los diferentes tipos de inmuebles presentes en tu dataset, desde Cocineta hasta Industria. Esto te da una idea de la diversidad del catálogo.
Conteo de valores en la columna 'Tipo':: Esta tabla te dice cuántos registros hay de cada tipo. Como esperábamos, Departamento es, por lejos, el tipo más común, seguido por Conjunto Comercial/Sala. Esto es útil para saber la composición de tu dataset.
Valores únicos en la columna 'Colonia':: Aquí ves la lista de todas las colonias representadas en el dataset. ¡Son bastantes (88 en total)!
Conteo de valores en la columna 'Colonia':: Similar al tipo de inmueble, esta tabla te muestra cuántos registros hay en cada colonia. Vemos que Santa Fe, Condesa y Centro Histórico son las colonias con más registros en este dataset. La notación ... indica que hay más colonias listadas, pero la salida se trunca por brevedad, lo cual es común cuando hay muchos valores únicos.
Ahora que sabemos qué tipo de datos tenemos en cada columna (numéricos, texto/categóricos) y ya exploramos las distribuciones básicas, un paso fundamental es aprender a seleccionar partes específicas de nuestro DataFrame. A menudo, no necesitamos trabajar con todas las columnas o todas las filas a la vez.

Podemos seleccionar:

Una sola columna: El resultado será una Serie de pandas.
Múltiples columnas: El resultado seguirá siendo un DataFrame de pandas.
'''