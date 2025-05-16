'''
Explicación del Código:
Leer el archivo CSV:

df_clientes = pd.read_csv(archivo_csv): Lee el archivo CSV en un DataFrame de pandas.
Crear un motor de base de datos SQLite en memoria:

engine = create_engine('sqlite:///:memory:'): Crea un motor de base de datos SQLite en memoria.
Guardar el DataFrame en una tabla de la base de datos:

df_clientes.to_sql('clientes', con=engine, index=False, if_exists='replace'): Guarda el DataFrame en una tabla llamada clientes en la base de datos SQLite.
Reflejar la tabla desde la base de datos:

clientes_table = Table('clientes', metadata, autoload_with=engine): Refleja la tabla clientes desde la base de datos.
Obtener información sobre la base de datos:

inspector = inspect(engine): Crea un objeto Inspector para obtener información sobre la base de datos.
inspector.get_table_names(): Obtiene los nombres de las tablas en la base de datos.
inspector.get_columns('clientes'): Obtiene información sobre las columnas de la tabla clientes.
Ejecutar una consulta SQL:

connection.execute(text("SELECT * FROM clientes LIMIT 5")): Ejecuta una consulta SQL para obtener los primeros registros de la tabla clientes.
'''

import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, inspect, text

# Ruta al archivo CSV
archivo_csv = 'clientes_banco.csv'

# Leer el archivo CSV en un DataFrame de pandas
df_clientes = pd.read_csv(archivo_csv)

# Crear un motor de base de datos SQLite en memoria
engine = create_engine('sqlite:///:memory:')

# Guardar el DataFrame en una tabla de la base de datos SQLite
df_clientes.to_sql('clientes', con=engine, index=False, if_exists='replace')

# Crear un objeto MetaData
metadata = MetaData()

# Reflejar la tabla 'clientes' desde la base de datos
clientes_table = Table('clientes', metadata, autoload_with=engine)

# Crear un objeto Inspector para obtener información sobre la base de datos
inspector = inspect(engine)

# Obtener los nombres de las tablas en la base de datos
print("Tablas en la base de datos:")
print(inspector.get_table_names())

# Obtener información sobre la tabla 'clientes'
print("\nInformación de la tabla 'clientes':")
print(inspector.get_columns('clientes'))

# Ejecutar una consulta SQL para obtener los primeros registros de la tabla 'clientes'
with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM clientes LIMIT 5"))
    print("\nPrimeros registros de la tabla 'clientes':")
    for row in result:
        print(row)

'''
Tablas en la base de datos:
['clientes']

Información de la tabla 'clientes':
[{'name': 'ID_Cliente', 'type': BIGINT(), 'nullable': True, 'default': None, 'primary_key': 0}, {'name': 'Edad', 'type': BIGINT(), 'nullable': True, 'default': None, 'primary_key': 0}, {'name': 'Grado_estudio', 'type': TEXT(), 'nullable': True, 'default': None, 'primary_key': 0}, {'name': 'Estado_civil', 'type': TEXT(), 'nullable': True, 'default': None, 'primary_key': 0}, {'name': 'Tamaño_familia', 'type': BIGINT(), 'nullable': True, 'default': None, 'primary_key': 0}, {'name': 'Categoria_de_renta', 'type': TEXT(), 'nullable': True, 'default': None, 'primary_key': 0}, {'name': 'Ocupacion', 'type': TEXT(), 'nullable': True, 'default': None, 'primary_key': 0}, {'name': 'Años_empleado', 'type': BIGINT(), 'nullable': True, 'default': None, 'primary_key': 0}, {'name': 'Rendimiento_anual', 'type': FLOAT(), 'nullable': True, 'default': None, 'primary_key': 0}, {'name': 'Tiene_carro', 'type': BIGINT(), 'nullable': True, 'default': None, 'primary_key': 0}, {'name': 'Vivienda', 'type': TEXT(), 'nullable': True, 'default': None, 'primary_key': 0}]

Primeros registros de la tabla 'clientes':
(5008804, 32, 'Nivel superior', 'Relación-estable', 2, 'Empleado', 'Otro', 12, 427500.0, 1, 'Departamento alquilado')
(5008805, 32, 'Nivel superior', 'Relación-estable', 2, 'Empleado', 'Otro', 12, 427500.0, 1, 'Departamento alquilado')
(5008806, 58, 'Nivel intermedio', 'Casado', 2, 'Empleado', 'Seguridad', 3, 112500.0, 1, 'Casa/Departamento propio')
(5008808, 52, 'Nivel intermedio', 'Soltero', 1, 'Business Partner', 'Ventas', 8, 270000.0, 0, 'Casa/Departamento propio')
(5008809, 52, 'Nivel intermedio', 'Soltero', 1, 'Business Partner', 'Ventas', 8, 270000.0, 0, 'Casa/Departamento propio')
                                                                                                                       
'''