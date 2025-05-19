'''
Para crear la base de datos local es necesario ejecutar los siguientes comandos. Este código 
consiste en importar la biblioteca sqlalchemy y crear un objeto engine que representa una conexión 
a una base de datos SQLite en memoria. El método create_engine se utiliza para crear el objeto 
engine y especificar la base de datos que se utilizará. En este caso, la base de datos es una base 
de datos SQLite en memoria, que se crea usando sqlite:///:memory::
'''

import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, inspect, text
from sqlalchemy.exc import SQLAlchemyError

# Ruta al archivo CSV
archivo_csv = 'clientes_banco.csv'

# Leer el archivo CSV en un DataFrame de pandas
df_clientes = pd.read_csv(archivo_csv)

# Crear un motor de base de datos SQLite en memoria
engine = create_engine('sqlite:///:memory:')

# Guardar el DataFrame en una tabla de la base de datos SQLite
df_clientes.to_sql('clientes', con=engine, index=False, if_exists='replace')

# 1. Actualizar el registro del cliente ID 6840104 cuyo rendimiento anual cambió a 300000
query_update = 'UPDATE clientes SET Rendimiento_anual=300000.0 WHERE ID_Cliente=6840104'
try:
    # Ejecutar la consulta de actualización
    r_set = engine.connect().execute(text(query_update))
    print("#Registros actualizados:", r_set.rowcount)
except SQLAlchemyError as e:
    print("Error al actualizar el registro:", e)

# 2. Eliminar el registro de cliente ID 5008809
query_delete = 'DELETE FROM clientes WHERE ID_Cliente=5008809'
try:
    # Ejecutar la consulta de eliminación
    r_set = engine.connect().execute(text(query_delete))
    print("#Registros borrados:", r_set.rowcount)
except SQLAlchemyError as e:
    print("Error al eliminar el registro:", e)

# 3. Crear un nuevo registro de cliente
query_insert = '''
INSERT INTO clientes (ID_Cliente, Edad, Grado_estudio, Estado_civil,
                      Tamaño_familia, Categoria_de_renta, Ocupacion, Años_empleado,
                      Rendimiento_anual, Tiene_carro, Vivienda)
VALUES (6850985, 33, "Doctorado", "Soltero", 1, "Empleado", "TI",
        2, 290000, 0, "Casa/Departamento propio")
'''
try:
    # Ejecutar la consulta de inserción
    r_set = engine.connect().execute(text(query_insert))
    print("#Registros insertados:", r_set.rowcount)
except SQLAlchemyError as e:
    print("Error al insertar el registro:", e)

# Verificar los cambios leyendo la tabla "clientes"
df_clientes_actualizado = pd.read_sql_table('clientes', con=engine.connect())
print("\nTabla de clientes actualizada:")
print(df_clientes_actualizado.head())

'''
#Registros actualizados: 1
#Registros borrados: 1
#Registros insertados: 1

Tabla de clientes actualizada:
   ID_Cliente  Edad     Grado_estudio  ... Rendimiento_anual  Tiene_carro                  Vivienda
0     5008804    32    Nivel superior  ...          427500.0            1    Departamento alquilado
1     5008805    32    Nivel superior  ...          427500.0            1    Departamento alquilado
2     5008806    58  Nivel intermedio  ...          112500.0            1  Casa/Departamento propio
3     5008808    52  Nivel intermedio  ...          270000.0            0  Casa/Departamento propio
4     5008810    52  Nivel intermedio  ...          270000.0            0  Casa/Departamento propio

[5 rows x 11 columns]


Explicación del Código:
Leer el archivo CSV:

df_clientes = pd.read_csv(archivo_csv): Lee el archivo CSV en un DataFrame de pandas.
Crear un motor de base de datos SQLite en memoria:

engine = create_engine('sqlite:///:memory:'): Crea un motor de base de datos SQLite en memoria.
Guardar el DataFrame en una tabla de la base de datos:

df_clientes.to_sql('clientes', con=engine, index=False, if_exists='replace'): Guarda el DataFrame en una tabla llamada clientes en la base de datos SQLite.
Actualizar el registro del cliente ID 6840104:

query_update = 'UPDATE clientes SET Rendimiento_anual=300000.0 WHERE ID_Cliente=6840104': Define la consulta SQL para actualizar el rendimiento anual del cliente con ID 6840104.
engine.connect().execute(text(query_update)): Ejecuta la consulta de actualización.
Eliminar el registro de cliente ID 5008809:

query_delete = 'DELETE FROM clientes WHERE ID_Cliente=5008809': Define la consulta SQL para eliminar el cliente con ID 5008809.
engine.connect().execute(text(query_delete)): Ejecuta la consulta de eliminación.
Crear un nuevo registro de cliente:

query_insert = 'INSERT INTO clientes (...) VALUES (...)': Define la consulta SQL para insertar un nuevo registro de cliente.
engine.connect().execute(text(query_insert)): Ejecuta la consulta de inserción.
Verificar los cambios leyendo la tabla "clientes":

pd.read_sql_table('clientes', con=engine.connect()): Lee la tabla clientes para verificar los cambios realizados.

'''

