import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Cargar datos
data = np.genfromtxt('citrus.csv', delimiter=',', skip_header=1, usecols=range(1,6))

print("Rango diámetros:", np.min(data[:,0]), "-", np.max(data[:,0]))
print("Rango pesos:", np.min(data[:,1]), "-", np.max(data[:,1]))

'''
Rango diámetros: 2.96 - 16.45
Rango pesos: 86.76 - 261.51
                           
'''