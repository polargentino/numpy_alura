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



