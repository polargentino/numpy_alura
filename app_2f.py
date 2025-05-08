import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Cargar datos
data = np.genfromtxt('citrus.csv', delimiter=',', skip_header=1, usecols=range(1,6))

# Configuración de estilo profesional
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelweight': 'bold',
    'figure.autolayout': True
})

# Procesamiento de datos
n_oranges = 5000
diam_naranja = data[:n_oranges, 0]  # Diámetros en cm
peso_naranja = data[:n_oranges, 1]  # Pesos en g
diam_toronja = data[n_oranges:, 0]
peso_toronja = data[n_oranges:, 1]

# Crear figura
fig, ax = plt.subplots(figsize=(12, 7))

# Scatter plots con parámetros optimizados
ax.scatter(diam_naranja, peso_naranja, color='#FF8C00', alpha=0.6,
          s=40, edgecolor='#FF4500', linewidth=0.6, 
          label=f'Naranjas (n={n_oranges})', marker='o')
ax.scatter(diam_toronja, peso_toronja, color='#DC143C', alpha=0.6,
          s=40, edgecolor='#8B0000', linewidth=0.6,
          label=f'Toronjas (n={len(data)-n_oranges})', marker='s')

# Ajustes de ejes precisos
ax.set_xlim(2.5, 17)
ax.set_ylim(80, 270)
ax.xaxis.set_major_locator(MultipleLocator(2))
ax.yaxis.set_major_locator(MultipleLocator(20))
ax.set_xlabel('Diámetro (cm)', fontsize=12, labelpad=10)
ax.set_ylabel('Peso (g)', fontsize=12, labelpad=10)

# Título y leyenda
ax.set_title('Relación Diámetro-Peso en Cítricos', pad=20, fontweight='bold')
ax.legend(title='Tipo de Fruta', title_fontsize='11')

# Estadísticas precisas
stats_text = (f"Estadísticas:\n"
              f"Naranjas:\n"
              f"• Diámetro: {np.mean(diam_naranja):.1f} ± {np.std(diam_naranja):.1f} cm\n"
              f"• Peso: {np.mean(peso_naranja):.1f} ± {np.std(peso_naranja):.1f} g\n\n"
              f"Toronjas:\n"
              f"• Diámetro: {np.mean(diam_toronja):.1f} ± {np.std(diam_toronja):.1f} cm\n"
              f"• Peso: {np.mean(peso_toronja):.1f} ± {np.std(peso_toronja):.1f} g")

ax.annotate(stats_text, xy=(0.02, 0.98), xycoords='axes fraction',
            ha='left', va='top', fontsize=10,
            bbox=dict(boxstyle='round', alpha=0.9, facecolor='white'))

# Líneas de tendencia
for diam, peso, color, label in [
    (diam_naranja, peso_naranja, '#FF8C00', 'Tendencia naranjas'),
    (diam_toronja, peso_toronja, '#DC143C', 'Tendencia toronjas')
]:
    z = np.polyfit(diam, peso, 1)
    ax.plot(diam, z[0]*diam + z[1], color=color, 
            linestyle='--', linewidth=1.5, alpha=0.7, label=label)

# Mostrar ecuación de tendencia
for diam, peso, color, xpos, ypos in [
    (diam_naranja, peso_naranja, '#FF8C00', 0.3, 0.15),
    (diam_toronja, peso_toronja, '#DC143C', 0.3, 0.05)
]:
    z = np.polyfit(diam, peso, 1)
    eq_text = f'y = {z[0]:.2f}x + {z[1]:.2f}'
    ax.text(xpos, ypos, eq_text, transform=ax.transAxes,
            color=color, fontsize=10, fontweight='bold')

plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.6)
plt.savefig('citrus_final_accurate.png', dpi=300, bbox_inches='tight')
plt.show()