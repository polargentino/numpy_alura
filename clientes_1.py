import pandas as pd
from sqlalchemy import create_engine, text

# Ruta al archivo CSV
archivo_csv = 'clientes_banco.csv'

# Leer el archivo CSV en un DataFrame de pandas
df_clientes = pd.read_csv(archivo_csv)

# Crear un motor de base de datos SQLite en memoria
engine = create_engine('sqlite:///:memory:')

# Guardar el DataFrame en una tabla de la base de datos SQLite
df_clientes.to_sql('clientes', con=engine, index=False, if_exists='replace')

# 1. Obtener el número de clientes por categoría de renta
with engine.connect() as connection:
    result = connection.execute(text("""
        SELECT Categoria_de_renta, COUNT(*) as Numero_de_clientes
        FROM clientes
        GROUP BY Categoria_de_renta
    """))
    print("\nNúmero de clientes por categoría de renta:")
    for row in result:
        print(row)

# 2. Obtener el promedio de rendimiento anual por ocupación
with engine.connect() as connection:
    result = connection.execute(text("""
        SELECT Ocupacion, AVG(Rendimiento_anual) as Promedio_rendimiento_anual
        FROM clientes
        GROUP BY Ocupacion
    """))
    print("\nPromedio de rendimiento anual por ocupación:")
    for row in result:
        print(row)

# 3. Obtener la distribución de clientes por estado civil
with engine.connect() as connection:
    result = connection.execute(text("""
        SELECT Estado_civil, COUNT(*) as Numero_de_clientes
        FROM clientes
        GROUP BY Estado_civil
    """))
    print("\nDistribución de clientes por estado civil:")
    for row in result:
        print(row)

'''
Número de clientes por categoría de renta:
('Business Partner', 100726)
('Empleado', 226059)
('Empleado estatal', 36183)
('Estudante', 17)
('Pensionista', 75478)

Promedio de rendimiento anual por ocupación:
('Alta tecnologia', 195712.25819302205)
('Baja calificación', 150334.3093457944)
('Chofer', 202061.708453134)
('Cocina', 155859.1631161754)
('Construcción Civil', 179870.90456375838)
('Contabilidad', 215129.96498748436)
('Corretor imobiliário', 223510.80691642652)
('Equipo principal', 190916.93180657315)
('Gerencia', 282099.8023141754)
('Limpieza', 147041.63802841006)
('Medicina', 168111.75565912118)
('Mesero', 158796.62162162163)
('Otro', 170867.76583468108)
('RRHH', 203620.68604651163)
('Secretaría', 169456.87866927593)
('Seguridad', 169835.1136619542)
('Servicio privado', 201626.4399421129)
('TI', 210958.7334437086)
('Ventas', 170907.81856225056)

Distribución de clientes por estado civil:
('Casado', 299768)
('Divorciado', 27249)
('Relación-estable', 36521)
('Soltero', 55255)
('Viudo', 19670)


Explicación de Mistral AI: 
-------------------------

Explicación del Código:
Leer el archivo CSV:

df_clientes = pd.read_csv(archivo_csv): Lee el archivo CSV en un DataFrame de pandas.
Crear un motor de base de datos SQLite en memoria:

engine = create_engine('sqlite:///:memory:'): Crea un motor de base de datos SQLite en memoria.
Guardar el DataFrame en una tabla de la base de datos:

df_clientes.to_sql('clientes', con=engine, index=False, if_exists='replace'): Guarda el DataFrame en una tabla llamada clientes en la base de datos SQLite.
Consulta 1: Número de clientes por categoría de renta:

SELECT Categoria_de_renta, COUNT(*) as Numero_de_clientes FROM clientes GROUP BY Categoria_de_renta: Esta consulta agrupa los clientes por su categoría de renta y cuenta el número de clientes en cada categoría.
connection.execute(text("...")): Ejecuta la consulta SQL y obtiene los resultados.
print("\nNúmero de clientes por categoría de renta:"): Imprime los resultados de la consulta.
Consulta 2: Promedio de rendimiento anual por ocupación:

SELECT Ocupacion, AVG(Rendimiento_anual) as Promedio_rendimiento_anual FROM clientes GROUP BY Ocupacion: Esta consulta calcula el promedio del rendimiento anual para cada ocupación.
connection.execute(text("...")): Ejecuta la consulta SQL y obtiene los resultados.
print("\nPromedio de rendimiento anual por ocupación:"): Imprime los resultados de la consulta.
Consulta 3: Distribución de clientes por estado civil:

SELECT Estado_civil, COUNT(*) as Numero_de_clientes FROM clientes GROUP BY Estado_civil: Esta consulta agrupa los clientes por su estado civil y cuenta el número de clientes en cada estado.
connection.execute(text("...")): Ejecuta la consulta SQL y obtiene los resultados.
print("\nDistribución de clientes por estado civil:"): Imprime los resultados de la consulta.

'''