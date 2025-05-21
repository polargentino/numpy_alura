import datetime
import pandas as pd

# creando un objeto datetime con la fecha y hora actual
ahora = datetime.datetime.now()

print("Fecha y hora actual:", ahora)
 
# creando un objeto date con la fecha de hoy
hoy = datetime.date.today()

print("Fecha de hoy:", hoy)

'''
Fecha y hora actual: 2025-05-20 18:51:27.858916
Fecha de hoy: 2025-05-20
'''

# creando dos objetos date con fechas diferentes
data_1 = datetime.date(2022, 1, 1)
data_2 = datetime.date(2023, 1, 1)

# calculando la diferencia entre las dos fechas
diferencia = data_2 - data_1

print("Diferencia entre las dos fechas:", diferencia)

'''
Diferencia entre las dos fechas: 365 days, 0:00:00
'''
# Creando el DataFrame con las informaciones
datos = pd.DataFrame({
    'Fecha de venta': ['01/01/2022', '05/02/2022', '10/03/2022', '15/04/2022','18/04/2022','20/04/2022'],
    'valor': [100, 150, 200, 250,80,180]
})

# Mostrando el DataFrame
print(datos)
'''
 Fecha de venta  valor
0     01/01/2022    100
1     05/02/2022    150
2     10/03/2022    200
3     15/04/2022    250
4     18/04/2022     80
5     20/04/2022    180
                       
'''
datos['Fecha de venta'] = pd.to_datetime(datos['Fecha de venta'], format='%d/%m/%Y')
print(datos['Fecha de venta'])
'''
0   2022-01-01
1   2022-02-05
2   2022-03-10
3   2022-04-15
4   2022-04-18
5   2022-04-20
Name: Fecha de venta, dtype: datetime64[ns]
'''