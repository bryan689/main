import pandas as pd
import matplotlib.pyplot as plt

# Leer los datos
column_names = ['Fecha', 'Hora', 'Precipitacion', 'Magnitud', 'Presion', 'Radiacion', 'Temperatura', 'Direccion', 'Atmosfera']
data = pd.read_csv('C:/Users/bryan/OneDrive/Documentos/datos/DATOS BOCANA.txt', sep=',', header=None, names=column_names)

# Crear el histograma
plt.figure(figsize=(10, 6))
plt.hist(data['Precipitacion'], bins=30, edgecolor='black', alpha=0.7, color='gray')
plt.title('Histograma de Precipitacion')
plt.xlabel('Precipitacion')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(data['Magnitud'], bins=30, edgecolor='black', alpha=0.7, color='gray')
plt.title('Histograma de Magnitud')
plt.xlabel('Magnitud')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(data['Presion'], bins=30, edgecolor='black', alpha=0.7, color='gray')
plt.title('Histograma de Presion')
plt.xlabel('Presion')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(data['Radiacion'], bins=30, edgecolor='black', alpha=0.7, color='gray')
plt.title('Histograma de Radiacion')
plt.xlabel('Radiacion')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(data['Temperatura'], bins=30, edgecolor='black', alpha=0.7, color='gray')
plt.title('Histograma de Temperatura')
plt.xlabel('Temperatura')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(data['Direccion'], bins=30, edgecolor='black', alpha=0.7, color='gray')
plt.title('Histograma de Direccion')
plt.xlabel('Direccion')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(data['Atmosfera'], bins=30, edgecolor='black', alpha=0.7, color='gray')
plt.title('Histograma de Atmosfera')
plt.xlabel('Atmosfera')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()