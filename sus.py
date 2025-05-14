import pandas as pd

# Ruta al archivo CSV en tu sistema Linux
file_path = '/home/pol/Escritorio/numpy_alura/datos_sus.csv'

# Leer el archivo CSV con los parámetros especificados
datos = pd.read_csv(
    file_path,
    encoding='ISO-8859-1',  # Codificación del archivo
    sep=';',                # Separador de valores
    skiprows=3,             # Ignorar las primeras tres líneas
    skipfooter=9,           # Ignorar las últimas nueve líneas
    engine='python'         # Motor utilizado para leer el archivo
)

# Mostrar las primeras filas del DataFrame para verificar que se haya leído correctamente
print(datos.head())

'''
  Unidade da Federação     2008/Jan     2008/Fev     2008/Mar  ...     2021/Jan     2021/Fev     2021/Mar          Total
0             Rondônia   1388528,39   2931283,42   1541682,52  ...   9266014,59   7730597,04  11023309,47   996411254,68
1                 Acre    902416,00   1497206,26   1794028,48  ...   3715723,12   3538427,92   4077045,92   450048530,47
2             Amazonas   4735529,42   7118990,57   8196635,49  ...  21430289,17  25917134,55  22032176,22  1917247936,05
3              Roraima    657889,53    777939,31    718688,03  ...   3266928,47   3519773,73   3985530,08   328876965,09
4                 Pará  18864744,11  19553758,20  21937342,70  ...  38354682,46  37688314,23  33276392,89  4705309002,29

[5 rows x 161 columns]
'''