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

# Guardar el DataFrame en un archivo CSV
pacientes_df.to_csv('pacientes_normalizados.csv', index=False)


'''
   ID Rango_edad Sexo_biologico  ... Salud_general  Horas_sueño                Problemas_salud
0  01      55-59          Mujer  ...     Muy buena            5  [Diabetes, Asma, Cancer_piel]
1  02     80 ó +          Mujer  ...     Muy buena            7                          [AVC]
2  03      65-69      Masculino  ...     Muy buena            8               [Diabetes, Asma]

[3 rows x 14 columns]
   ID Rango_edad Sexo_biologico  ... Salud_general  Horas_sueño                Problemas_salud
0  01      55-59          Mujer  ...     Muy buena            5  [Diabetes, Asma, Cancer_piel]
2  03      65-69      Masculino  ...     Muy buena            8               [Diabetes, Asma]

[2 rows x 14 columns]
                        

pacientes_normalizados.csv:
--------------------------
ID,Rango_edad,Sexo_biologico,Raza,IMC,Fumador,Consumo_alcohol,Salud_física,Salud_mental,Dificultad_caminar,Actividad_física,Salud_general,Horas_sueño,Problemas_salud
01,55-59,Mujer,Blanca,16.6,Sí,No,3,30,No,Sí,Muy buena,5,"['Diabetes', 'Asma', 'Cancer_piel']"
02,80 ó +,Mujer,Blanca,20.34,No,No,0,0,No,Sí,Muy buena,7,['AVC']
03,65-69,Masculino,Blanca,26.58,Sí,No,20,30,No,Sí,Muy buena,8,"['Diabetes', 'Asma']"

'''