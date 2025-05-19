import pandas as pd
import matplotlib.pyplot as plt

# Ruta al archivo Excel
file_path = 'C:/Users/bryan/OneDrive/Documentos/datos/Estudiantes_programas_academicos_y_Extension_20250316.xlsx'
excel_data = pd.ExcelFile(file_path)

# Leer la hoja correspondiente
df = excel_data.parse('Estudiantes_programas_academico')

# Convertir columnas a numéricas
numeric_columns = [
    "NUMERO MATERIAS INSCRITAS",
    "NUMERO MATERIAS APROBADAS",
    "ESTRATO",
    "SEMESTRE"
]
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors="coerce")

# Calcular materias reprobadas
df["MATERIAS REPROBADAS"] = df["NUMERO MATERIAS INSCRITAS"] - df["NUMERO MATERIAS APROBADAS"]

# Crear histograma de materias inscritas
plt.figure(figsize=(10, 6)) 
plt.hist(df["NUMERO MATERIAS INSCRITAS"].dropna(), bins=30, edgecolor='black', alpha=0.7, color='lightblue')
plt.title('Histograma de Materias Inscritas')
plt.xlabel('Materias Inscritas')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Crear histograma de materias aprobadas
plt.figure(figsize=(10, 6))
plt.hist(df["NUMERO MATERIAS APROBADAS"].dropna(), bins=30, edgecolor='black', alpha=0.7, color='lightgreen')
plt.title('Histograma de Materias Aprobadas')
plt.xlabel('Materias Aprobadas')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Crear histograma de materias reprobadas
plt.figure(figsize=(10, 6))
plt.hist(df["MATERIAS REPROBADAS"].dropna(), bins=30, edgecolor='black', alpha=0.7, color='salmon')
plt.title('Histograma de Materias Reprobadas')
plt.xlabel('Materias Reprobadas')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Crear histograma de semestre
plt.figure(figsize=(10, 6))
plt.hist(df["SEMESTRE"].dropna(), bins=30, edgecolor='black', alpha=0.7, color='skyblue')
plt.title('Histograma de Semestre')
plt.xlabel('Semestre')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Crear histograma de sexo biológico
plt.figure(figsize=(10, 6))
df["SEXO BIOLOGICO"].value_counts().plot(kind='bar', color='lightgreen', edgecolor='black', alpha=0.7)
plt.title('Histograma de Sexo Biológico')
plt.xlabel('Sexo Biológico')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Crear histograma de programa
plt.figure(figsize=(10, 6))
df["PROGRAMA"].value_counts().plot(kind='bar', color='lightcoral', edgecolor='black', alpha=0.7)
plt.title('Histograma de Programa')
plt.xlabel('Programa')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Crear histograma de país de nacimiento
plt.figure(figsize=(10, 6))
df["PAIS NACIMIENTO"].value_counts().plot(kind='bar', color='gold', edgecolor='black', alpha=0.7)
plt.title('Histograma de País de Nacimiento')
plt.xlabel('País de Nacimiento')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Crear histograma de departamento de nacimiento
plt.figure(figsize=(10, 6))
df["DEPARTAMENTO NACIMIENTO"].value_counts().plot(kind='bar', color='gold', edgecolor='black', alpha=0.7)
plt.title('Histograma de departamento de Nacimiento')
plt.xlabel('Departamento de Nacimiento')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Crear histograma de estrato
plt.figure(figsize=(10, 6))
df["ESTRATO"].value_counts().plot(kind='bar', color='lightblue', edgecolor='black', alpha=0.7)
plt.title('Histograma de Estrato')
plt.xlabel('Estrato')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()