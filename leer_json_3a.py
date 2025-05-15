'''
Explicación del código:
Convertir el DataFrame a una lista de diccionarios:

pacientes_dict = pacientes_df.to_dict(orient='records'): Convierte el DataFrame en una lista de diccionarios.
Guardar el archivo JSON:

with open('pacientes_normalizados_1.json', 'w', encoding='utf-8') as archivo_json:: Abre (o crea) un archivo llamado pacientes_normalizados_1.json en modo escritura con codificación UTF-8.
json.dump(pacientes_dict, archivo_json, ensure_ascii=False, indent=4): Escribe los datos en el archivo JSON. El parámetro ensure_ascii=False permite caracteres no ASCII, y indent=4 añade indentación para mejorar la legibilidad.
Con estos cambios, deberías poder guardar el DataFrame en un archivo JSON sin secuencias de escape Unicode para caracteres especiales.
'''
import pandas as pd
import json

# Leer el archivo JSON
datos_pacientes_2 = pd.read_json('pacientes_2.json')

# Normalizar la columna de diccionarios
pacientes_df = pd.json_normalize(datos_pacientes_2['Pacientes'])

# Imprimir el DataFrame normalizado
print(pacientes_df.head())

# Filtrar pacientes con diabetes
pacientes_con_diabetes = pacientes_df[pacientes_df['Problemas_salud'].apply(lambda x: 'Diabetes' in x)]
print(pacientes_con_diabetes)

# Convertir el DataFrame a una lista de diccionarios
pacientes_dict = pacientes_df.to_dict(orient='records')

# Guardar el DataFrame en un archivo JSON con ensure_ascii=False
with open('pacientes_normalizados_1.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(pacientes_dict, archivo_json, ensure_ascii=False, indent=4)

'''
   ID Rango_edad Sexo_biologico    Raza  ...  Actividad_física Salud_general Horas_sueño                Problemas_salud
0  01      55-59          Mujer  Blanca  ...                Sí     Muy buena           5  [Diabetes, Asma, Cancer_piel]
1  02     80 ó +          Mujer  Blanca  ...                Sí     Muy buena           7                          [AVC]
2  03      65-69      Masculino  Blanca  ...                Sí     Muy buena           8               [Diabetes, Asma]

[3 rows x 14 columns]
   ID Rango_edad Sexo_biologico    Raza  ...  Actividad_física Salud_general Horas_sueño                Problemas_salud
0  01      55-59          Mujer  Blanca  ...                Sí     Muy buena           5  [Diabetes, Asma, Cancer_piel]
2  03      65-69      Masculino  Blanca  ...                Sí     Muy buena           8               [Diabetes, Asma]

[2 rows x 14 columns]


[
    {
        "ID": "01",
        "Rango_edad": "55-59",
        "Sexo_biologico": "Mujer",
        "Raza": "Blanca",
        "IMC": 16.6,
        "Fumador": "Sí",
        "Consumo_alcohol": "No",
        "Salud_física": 3,
        "Salud_mental": 30,
        "Dificultad_caminar": "No",
        "Actividad_física": "Sí",
        "Salud_general": "Muy buena",
        "Horas_sueño": 5,
        "Problemas_salud": [
            "Diabetes",
            "Asma",
            "Cancer_piel"
        ]
    },
    {
        "ID": "02",
        "Rango_edad": "80 ó +",
        "Sexo_biologico": "Mujer",
        "Raza": "Blanca",
        "IMC": 20.34,
        "Fumador": "No",
        "Consumo_alcohol": "No",
        "Salud_física": 0,
        "Salud_mental": 0,
        "Dificultad_caminar": "No",
        "Actividad_física": "Sí",
        "Salud_general": "Muy buena",
        "Horas_sueño": 7,
        "Problemas_salud": [
            "AVC"
        ]
    },
    {
        "ID": "03",
        "Rango_edad": "65-69",
        "Sexo_biologico": "Masculino",
        "Raza": "Blanca",
        "IMC": 26.58,
        "Fumador": "Sí",
        "Consumo_alcohol": "No",
        "Salud_física": 20,
        "Salud_mental": 30,
        "Dificultad_caminar": "No",
        "Actividad_física": "Sí",
        "Salud_general": "Muy buena",
        "Horas_sueño": 8,
        "Problemas_salud": [
            "Diabetes",
            "Asma"
        ]
    }
]




'''