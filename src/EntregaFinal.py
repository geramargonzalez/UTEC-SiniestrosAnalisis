

#Importamos la base de datos preprocesada anteriormente llamada "preprocesamiento_siniestros2022.csv"
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.pyplot as plt

# Graficamos Diagramas de caja
import plotly.express as px

#EL FILE PATH SE DEBE AJUSTAR AL CAMINO DE CADA UNO!
file_path = "/content/drive/MyDrive/UTEC - Python/Equipo/preprocesamiento_siniestros2022.csv"
#EL FILE PATH SE DEBE AJUSTAR AL CAMINO DE CADA UNO!
file_path = "preprocesamiento_siniestros2022.csv"  # Ajusta esta ruta a la ubicación de tu archivo
df = pd.read_csv(file_path)
df.head()

# Verificamos las estadisticas principales
df.describe()

#Chequemos los nombres de las columnas
df.columns

# ---------------------------------------------------------------------

# Elegimos un estilo y paleta compatible con el daltonismo
sns.set(style="whitegrid", palette="colorblind")

color = sns.color_palette("colorblind")[0]  # azul fuerte accesible

# Creamos el histograma de la variable "EDAD"
plt.figure(figsize=(8, 4))
sns.histplot(df['Edad'], bins=30, kde=True, color=color)

# Le ponemos etiquetas y título
plt.title('Distribución de Edad en Siniestros', fontsize=16)
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()

# ---------------------------------------------------------------------

# Elegimos un estilo para daltonismo
sns.set(style="whitegrid", palette="colorblind")

# Creamos la boxplot de la variable "EDAD"
plt.figure(figsize=(8, 4))
sns.boxplot(x=df['Edad'], color='skyblue')

# Agragamos títulos y etiquetas
plt.title('Diagrama de Caja de Edad', fontsize=16)
plt.xlabel('Edad')
plt.show()

# ---------------------------------------------------------------------

# Elegimos un estilo accesible
sns.set(style="whitegrid", palette="colorblind")

# Paleta colorblind personalizada (usamos colores distintos)
colores = sns.color_palette("colorblind")

# Gráficamos la variable 'ROL'
plt.figure(figsize=(6, 5))
ax = sns.countplot(data=df, x='Rol')
ax.set_title('Distribución de Rol en Siniestros')
ax.set_xlabel('')
ax.set_ylabel('Frecuencia')
plt.xticks(rotation=45, ha='right')

for p in ax.patches:
    height = int(p.get_height())
    ax.text(p.get_x() + p.get_width() / 2, height + 1, str(height),
            ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

# ---------------------------------------------------------------------

# Elegimos estilo y paleta
sns.set(style="whitegrid", palette="colorblind")
colores = sns.color_palette("colorblind")

# Hacemos un conteo por categoría
conteo = df['Rol'].value_counts()

# Hacemos un grafico circular de 'ROL' con el peso de cada uno en el total
plt.figure(figsize=(6, 6))
plt.pie(conteo, labels=conteo.index, autopct='%1.1f%%', startangle=140, colors=colores[:len(conteo)])
plt.title('Distribución de Rol en Siniestros')
plt.axis('equal')  # Mantener el círculo
plt.tight_layout()
plt.show()

# ---------------------------------------------------------------------

# Gráfico para 'TIPO DE RESULTADO'
plt.figure(figsize=(6, 5))
ax = sns.countplot(data=df, x='Tipo_de_resultado', color=colores[1])
ax.set_title('Distribución de Tipo de Resultado')
ax.set_xlabel('')
ax.set_ylabel('Frecuencia')
plt.xticks(rotation=45, ha='right')

for p in ax.patches:
    height = int(p.get_height())
    ax.text(p.get_x() + p.get_width() / 2, height + 1, str(height),
            ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

# ---------------------------------------------------------------------

# Gráfico para 'TIPO DE SINIESTRO'
plt.figure(figsize=(6, 5))
ax = sns.countplot(data=df, x='Tipo_de_siniestro', color=colores[2])
ax.set_title('Distribución de Tipo de Siniestro')
ax.set_xlabel('')
ax.set_ylabel('Frecuencia')
plt.xticks(rotation=45, ha='right')

for p in ax.patches:
    height = int(p.get_height())
    ax.text(p.get_x() + p.get_width() / 2, height + 1, str(height),
            ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

# ---------------------------------------------------------------------

# Gráfico para 'DIA DE LA SEMANA'
plt.figure(figsize=(6, 5))
ax = sns.countplot(data=df, x='Dia_de_la_semana', color=colores[3])
ax.set_title('Distribución por Día de la Semana')
ax.set_xlabel('')
ax.set_ylabel('Frecuencia')
plt.xticks(rotation=45, ha='right')

for p in ax.patches:
    height = int(p.get_height())
    ax.text(p.get_x() + p.get_width() / 2, height + 1, str(height),
            ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()


# ---------------------------------------------------------------------

# Gráfico para 'SEXO'
plt.figure(figsize=(6, 5))
ax = sns.countplot(data=df, x='Sexo', color=colores[4])
ax.set_title('Distribución por Sexo')
ax.set_xlabel('')
ax.set_ylabel('Frecuencia')
plt.xticks(rotation=45, ha='right')

for p in ax.patches:
    height = int(p.get_height())
    ax.text(p.get_x() + p.get_width() / 2, height + 1, str(height),
            ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

# ---------------------------------------------------------------------


# Elegimos estilo y paleta
sns.set(style="whitegrid", palette="colorblind")
colores = sns.color_palette("colorblind")

# Conteo por categoría
conteo = df['Sexo'].value_counts()

# Creamos la figura
fig, ax = plt.subplots(figsize=(6, 6))

# Creamos el gráfico de dona
wedges, texts, autotexts = ax.pie(
    conteo,
    labels=None,  # No usamos etiquetas directamente
    autopct='%1.1f%%',
    startangle=140,
    colors=colores[:len(conteo)],
    wedgeprops=dict(width=0.5),
    textprops={'color': 'white', 'fontsize': 12}
)

# Añadimos leyenda al costado para evitar solapamiento
ax.legend(wedges, conteo.index, title='Sexo', loc='center left', bbox_to_anchor=(1, 0.5))

# Agregamos título separado del gráfico
plt.title('Distribución de Sexo', pad=20)
plt.axis('equal')  # Mantener forma circular
plt.tight_layout()
plt.show()

# ---------------------------------------------------------------------


# Gráfico para 'TIPO DE VEHICULO'
plt.figure(figsize=(6, 5))
ax = sns.countplot(data=df, x='Tipo_de_Vehiculo', color=colores[5])
ax.set_title('Distribución de Tipo de Vehículo')
ax.set_xlabel('')
ax.set_ylabel('Frecuencia')
plt.xticks(rotation=45, ha='right')

for p in ax.patches:
    height = int(p.get_height())
    ax.text(p.get_x() + p.get_width() / 2, height + 1, str(height),
            ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

# ---------------------------------------------------------------------

# Gráfico para 'MOMENTO DIA'
plt.figure(figsize=(6, 5))
ax = sns.countplot(data=df, x='Momento_dia', color=colores[6])
ax.set_title('Distribución por Momento del Día')
ax.set_xlabel('')
ax.set_ylabel('Frecuencia')
plt.xticks(rotation=45, ha='right')

for p in ax.patches:
    height = int(p.get_height())
    ax.text(p.get_x() + p.get_width() / 2, height + 1, str(height),
            ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

# ---------------------------------------------------------------------


# Gráfico para 'HORA PICO'
plt.figure(figsize=(6, 5))
ax = sns.countplot(data=df, x='Hora_pico', color=colores[7])
ax.set_title('Distribución por Hora Pico')
ax.set_xlabel('')
ax.set_ylabel('Frecuencia')
plt.xticks(rotation=45, ha='right')

for p in ax.patches:
    height = int(p.get_height())
    ax.text(p.get_x() + p.get_width() / 2, height + 1, str(height),
            ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

# ---------------------------------------------------------------------


# Contamos frecuencia de cada categoría
hora_pico_counts = df['Hora_pico'].value_counts().sort_index()
labels = ['No es hora pico', 'Hora pico']
sizes = hora_pico_counts.values

# Elegimos colores
colors = ['#1f77b4', '#ff7f0e']  # azul y naranja

# Creamos gráfico de pastel
plt.figure(figsize=(6, 6))
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    textprops={'fontsize': 12}
)
plt.title('Distribución de Siniestros por Hora Pico', fontsize=14)
plt.axis('equal')  # Mantiene forma circular
plt.show()

# ---------------------------------------------------------------------