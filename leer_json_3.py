import pandas as pd

# Leer el archivo JSON
datos_pacientes_2 = pd.read_json('pacientes_2.json')

# Normalizar la columna de diccionarios
pacientes_df = pd.json_normalize(datos_pacientes_2['Pacientes'])

# Imprimir el DataFrame normalizado
print(pacientes_df.head())

# Filtrar pacientes con diabetes
pacientes_con_diabetes = pacientes_df[pacientes_df['Problemas_salud'].apply(lambda x: 'Diabetes' in x)]
print(pacientes_con_diabetes)

# Guardar el DataFrame en un archivo JSON
pacientes_df.to_json('pacientes_normalizados.json', orient='records', indent=4)

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
        "ID":"01",
        "Rango_edad":"55-59",
        "Sexo_biologico":"Mujer",
        "Raza":"Blanca",
        "IMC":16.6,
        "Fumador":"S\u00ed",
        "Consumo_alcohol":"No",
        "Salud_f\u00edsica":3,
        "Salud_mental":30,
        "Dificultad_caminar":"No",
        "Actividad_f\u00edsica":"S\u00ed",
        "Salud_general":"Muy buena",
        "Horas_sue\u00f1o":5,
        "Problemas_salud":[
            "Diabetes",
            "Asma",
            "Cancer_piel"
        ]
    },
    {
        "ID":"02",
        "Rango_edad":"80 \u00f3 +",
        "Sexo_biologico":"Mujer",
        "Raza":"Blanca",
        "IMC":20.34,
        "Fumador":"No",
        "Consumo_alcohol":"No",
        "Salud_f\u00edsica":0,
        "Salud_mental":0,
        "Dificultad_caminar":"No",
        "Actividad_f\u00edsica":"S\u00ed",
        "Salud_general":"Muy buena",
        "Horas_sue\u00f1o":7,
        "Problemas_salud":[
            "AVC"
        ]
    },
    {
        "ID":"03",
        "Rango_edad":"65-69",
        "Sexo_biologico":"Masculino",
        "Raza":"Blanca",
        "IMC":26.58,
        "Fumador":"S\u00ed",
        "Consumo_alcohol":"No",
        "Salud_f\u00edsica":20,
        "Salud_mental":30,
        "Dificultad_caminar":"No",
        "Actividad_f\u00edsica":"S\u00ed",
        "Salud_general":"Muy buena",
        "Horas_sue\u00f1o":8,
        "Problemas_salud":[
            "Diabetes",
            "Asma"
        ]
    }
]



Lo que estás viendo en el archivo JSON no son errores de ortografía, sino secuencias de escape Unicode. Estas secuencias se utilizan para representar caracteres especiales que no son parte del conjunto de caracteres ASCII estándar. Aquí hay una explicación de lo que estás viendo:

\u00ed: Representa la letra "í".
\u00f3: Representa la letra "ó".
\u00f1: Representa la letra "ñ".
¿Por qué aparecen estas secuencias?
Cuando guardas un archivo JSON con caracteres no ASCII (como letras acentuadas o la "ñ"), estos caracteres se representan utilizando secuencias de escape Unicode para asegurar que el archivo JSON sea válido y pueda ser interpretado correctamente por cualquier sistema, independientemente de su configuración de codificación.
'''