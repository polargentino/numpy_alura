import numpy as np
import matplotlib.pyplot as plt

# Cargar datos
data = np.genfromtxt('citrus.csv', delimiter=',', skip_header=1, usecols=range(1,6))

# Configuración de estilo
plt.style.use('seaborn-v0_8')
plt.rcParams['font.size'] = 12

# Dividir datos
n_oranges = 5000
diam_naranja = data[:n_oranges, 0]  # Diámetro (col 0)
peso_naranja = data[:n_oranges, 1]  # Peso (col 1)
diam_toronja = data[n_oranges:, 0]
peso_toronja = data[n_oranges:, 1]

# Crear figura
fig, ax = plt.subplots(figsize=(12, 7))

# Scatter plots con parámetros mejorados
ax.scatter(diam_naranja, peso_naranja, color='#FFA500', alpha=0.6, 
           s=50, edgecolor='#FF8C00', linewidth=0.5, label='Naranjas')
ax.scatter(diam_toronja, peso_toronja, color='#FF4500', alpha=0.6, 
           s=50, edgecolor='#8B0000', linewidth=0.5, label='Toronjas')

# Ajustes de ejes
ax.set_xlim(2, 5)
ax.set_ylim(80, 100)
ax.set_xlabel('Diámetro (cm)', fontweight='bold')
ax.set_ylabel('Peso (g)', fontweight='bold')
ax.set_title('Relación entre Diámetro y Peso de Cítricos', 
             fontsize=14, pad=20, fontweight='bold')

# Grid y leyenda
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(title='Tipo de fruta', title_fontsize='13')

# Añadir anotaciones estadísticas
stats_text = f"""Datos estadísticos:
Naranjas: {n_oranges} muestras
Toronjas: {len(data)-n_oranges} muestras
"""
ax.annotate(stats_text, xy=(0.02, 0.98), xycoords='axes fraction',
            ha='left', va='top', bbox=dict(boxstyle='round', alpha=0.8, facecolor='white'))

plt.tight_layout()
plt.savefig('citrus_plot_enhanced.png', dpi=300)
plt.show()