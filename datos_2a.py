import datetime

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
