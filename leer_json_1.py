import pandas as pd

# Leer el archivo JSON
datos_pacientes_2 = pd.read_json('pacientes_2.json')

# Normalizar la columna de diccionarios
pacientes_df = pd.json_normalize(datos_pacientes_2['Pacientes'])

# Imprimir el DataFrame normalizado
print(pacientes_df.head())

'''
   ID Rango_edad Sexo_biologico  ... Salud_general  Horas_sueño                Problemas_salud
0  01      55-59          Mujer  ...     Muy buena            5  [Diabetes, Asma, Cancer_piel]
1  02     80 ó +          Mujer  ...     Muy buena            7                          [AVC]
2  03      65-69      Masculino  ...     Muy buena            8               [Diabetes, Asma]

[3 rows x 14 columns]



El resultado que has mostrado es un DataFrame de pandas que ha sido normalizado correctamente a partir de un archivo JSON con una estructura anidada. Aquí tienes una explicación de cómo se ha logrado esto y cómo puedes trabajar con este DataFrame:

Explicación del DataFrame
El DataFrame tiene las siguientes columnas:

ID: Identificador único para cada paciente.
Rango_edad: Rango de edad del paciente.
Sexo_biologico: Sexo biológico del paciente.
...: Otras columnas que no se muestran en el ejemplo.
Salud_general: Una descripción de la salud general del paciente.
Horas_sueño: Número de horas de sueño del paciente.
Problemas_salud: Una lista de problemas de salud que tiene el paciente.

'''