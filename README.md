#  UTEC - Análisis de Siniestros de Tránsito (Montevideo 2022)

Proyecto académico desarrollado en el marco del curso de Python de **UTEC (Universidad Tecnológica del Uruguay)**.  
El objetivo es aplicar técnicas de preprocesamiento y análisis exploratorio de datos (EDA) sobre el conjunto de datos de siniestros de tránsito ocurridos en Montevideo durante el año 2022.

---

## 📋 Tabla de Contenidos

1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Estructura del Repositorio](#estructura-del-repositorio)
3. [Requisitos Previos](#requisitos-previos)
4. [Fuente de Datos](#fuente-de-datos)
5. [Paso 1 – Importación de Datos](#paso-1--importación-de-datos)
6. [Paso 2 – Evaluación de Calidad de Datos](#paso-2--evaluación-de-calidad-de-datos)
7. [Paso 3 – Tamaño del Conjunto de Datos](#paso-3--tamaño-del-conjunto-de-datos)
8. [Paso 4 – Preprocesamiento y Limpieza](#paso-4--preprocesamiento-y-limpieza)
9. [Paso 5 – Estadísticos Descriptivos](#paso-5--estadísticos-descriptivos)
10. [Paso 6 – Datos Duplicados y Nulos](#paso-6--datos-duplicados-y-nulos)
11. [Paso 7 – Análisis Exploratorio y Visualización](#paso-7--análisis-exploratorio-y-visualización)
12. [Cómo Ejecutar el Proyecto](#cómo-ejecutar-el-proyecto)
13. [Tecnologías Utilizadas](#tecnologías-utilizadas)

---

## Descripción del Proyecto

Este proyecto analiza los siniestros de tránsito registrados en Montevideo, Uruguay, durante el año 2022. A través de técnicas de ciencia de datos se busca identificar patrones relacionados con:

- Distribución de edades de los involucrados
- Roles de las personas (conductor, pasajero, peatón)
- Tipos de vehículos involucrados
- Resultados de los accidentes (ileso, herido leve, herido grave, fallecido)
- Distribución temporal (día de la semana, hora del día, hora pico)
- Distribución por sexo
- Tipos de siniestros más frecuentes

---

## Estructura del Repositorio

```
UTEC-SiniestrosAnalisis/
├── README.md                      # Documentación del proyecto
└── src/
    ├── SiniestrosDATABASE.py      # Script de preprocesamiento y limpieza de datos
    ├── EntregaFinal.py            # Script de análisis exploratorio y visualizaciones
    ├── dataFrame.py               # Ejercicios de aprendizaje con Pandas DataFrames
    ├── clase6Pandas.py            # Ejercicios de aprendizaje con Pandas Series
    └── holaMundo.py               # Script de prueba inicial
```

---

## Requisitos Previos

Asegurarse de tener instalado **Python 3.8+** y las siguientes librerías:

```bash
pip install pandas numpy matplotlib seaborn plotly
```

---

## Fuente de Datos

- **Dataset**: Siniestros de tránsito Montevideo 2022
- **Proveedor**: Intendencia de Montevideo – Catálogo de Datos Abiertos
- **URL de descarga**:
  ```
  https://ckan-data.montevideo.gub.uy/dataset/d8b39296-5fcf-4a8e-ac9f-d02a24698b97/resource/f1157e84-9577-4d8f-b2f3-92c1d720ae93/download/siniestros2022.csv
  ```
- **Formato**: CSV
- **Observaciones originales**: 7.802 filas × 19 columnas

### Variables del Dataset

| Variable | Tipo | Descripción |
|---|---|---|
| `Fecha` | Fecha | Fecha del siniestro |
| `Hora` | Hora | Hora en que ocurrió |
| `Dia_de_la_semana` | Categórica | Día de la semana |
| `Momento_dia` | Categórica | Momento del día (mañana, tarde, noche) |
| `Hora_pico` | Binaria | Si ocurrió en hora pico (1) o no (0) |
| `Rol` | Categórica | Rol de la persona involucrada |
| `Tipo_de_resultado` | Categórica | Resultado del accidente |
| `Tipo_de_siniestro` | Categórica | Clasificación del siniestro |
| `Sexo` | Categórica | Sexo de la persona |
| `Edad` | Numérica | Edad de la persona |
| `Tipo_de_Vehiculo` | Categórica | Tipo de vehículo involucrado |
| `Zona` | Categórica | Zona urbana o rural |
| `Calle` | Texto | Nombre de la calle |
| `Localidad` | Categórica | Localidad del accidente |
| `Usa_casco` | Categórica | *(Eliminada por exceso de nulos)* |
| `Usa_cinturon` | Categórica | *(Eliminada por exceso de nulos)* |

---

## Paso 1 – Importación de Datos

**Script**: `src/SiniestrosDATABASE.py`

El dataset se importa directamente desde la URL pública del catálogo de datos de Montevideo usando `pandas.read_csv()`:

```python
import pandas as pd
import numpy as np

dataUy = pd.read_csv('https://ckan-data.montevideo.gub.uy/.../siniestros2022.csv')
dataUy.head()
```

---

## Paso 2 – Evaluación de Calidad de Datos

**Script**: `src/SiniestrosDATABASE.py`

Se realiza una evaluación de calidad aplicando las siguientes técnicas:

### 2.1 Normalización de Nombres de Columnas

Se estandarizan los nombres de columnas reemplazando espacios por guiones bajos (`_`) y corrigiendo problemas de codificación de caracteres especiales:

```python
def clean_column_name(col):
    col = col.strip().replace(" ", "_")
    return col

dataUy.columns = [clean_column_name(col) for col in dataUy.columns]

# Corrección de errores de codificación
dataUy.rename(columns={
    'Usa_cinturI²n': 'Usa_cinturon',
    'DI²a_de_la_semana': 'Dia_de_la_semana'
}, inplace=True)
```

### 2.2 Eliminación de Espacios en Blanco

```python
dataUy = dataUy.applymap(lambda x: x.strip() if isinstance(x, str) else x)
```

### 2.3 Tratamiento de Valores Faltantes

Los datos faltantes no aparecen como `NaN`, sino como la cadena `"SIN DATOS"`. Se los reemplaza correctamente:

- **Variable numérica `Edad`**: se reemplaza `"SIN DATOS"` por `NaN` y se convierte a `float`.
- **Variables categóricas** (`Usa_casco`, `Calle`, `Localidad`, `Tipo_de_Vehiculo`, `Zona`, `Usa_cinturon`, `Sexo`): se reemplaza `"SIN DATOS"` por `None`.

```python
dataUy['Edad'] = dataUy['Edad'].replace('SIN DATOS', np.nan).astype(float)

columns_to_replace = ['Usa_casco', 'Calle', 'Localidad', 'Tipo_de_Vehiculo', 'Zona', 'Usa_cinturon', 'Sexo']
for col in columns_to_replace:
    dataUy[col] = dataUy[col].replace('SIN DATOS', None)
```

### 2.4 Conversión de Variables de Fecha y Hora

```python
dataUy['Fecha'] = pd.to_datetime(dataUy['Fecha'], format='mixed')
dataUy['Hora']  = pd.to_datetime(dataUy['Hora'], format='%H').dt.time

# Variable combinada Fecha + Hora
dataUy['Fecha_Hora'] = dataUy.apply(
    lambda row: pd.Timestamp.combine(row['Fecha'], row['Hora']), axis=1
)
```

---

## Paso 3 – Tamaño del Conjunto de Datos

```python
print(dataUy.shape)
# Resultado: (7802, 19)
# 7.802 observaciones × 19 variables originales
```

---

## Paso 4 – Preprocesamiento y Limpieza

**Script**: `src/SiniestrosDATABASE.py`

### 4.1 Eliminación de Columnas con Alta Proporción de Nulos

Se identificó que `Usa_cinturon` y `Usa_casco` tienen más del 20% de datos nulos, por lo que se eliminan:

```python
print(dataUy.isnull().sum() * 100 / len(dataUy))

dataUy = dataUy.drop(columns='Usa_cinturon')
dataUy = dataUy.drop(columns='Usa_casco')
# Dataset resultante: 7.802 observaciones × 17 variables
```

### 4.2 Corrección de Errores Tipográficos en Variables Categóricas

Se verifican los valores únicos de cada variable categórica contra la metadata oficial y se corrigen los errores encontrados:

```python
# Error tipográfico en Tipo_de_siniestro
dataUy['Tipo_de_siniestro'] = dataUy['Tipo_de_siniestro'].replace(
    'COLISION CON OBSTICULO EN CALZADA',
    'COLISION CON OBSTACULO EN CALZADA'
)

# Error tipográfico en Dia_de_la_semana
dataUy['Dia_de_la_semana'] = dataUy['Dia_de_la_semana'].replace('SIBADO', 'SABADO')
```

### 4.3 Homogeneización de Tipo de Vehículo

La variable `Tipo_de_Vehiculo` contiene valores extra no contemplados en la metadata. Se aceptan los que aportan información relevante (CAMIONETA, MOTOCICLETA, CICLOMOTOR, TRICICLO) y se reclasifican los inválidos como `OTRO`:

```python
dataUy['Tipo_de_Vehiculo'] = dataUy['Tipo_de_Vehiculo'].replace('PEATON', 'OTRO')
dataUy['Tipo_de_Vehiculo'] = dataUy['Tipo_de_Vehiculo'].replace('CHAPA MATRICULA', 'OTRO')
```

### 4.4 Exportación del Dataset Preprocesado

El dataset limpio se exporta como CSV para ser utilizado en la etapa de análisis:

```python
dataUy.to_csv('preprocesamiento_siniestros2022.csv', index=False)
```

---

## Paso 5 – Estadísticos Descriptivos

```python
dataUy.describe()
```

Permite obtener estadísticos principales (media, desvío estándar, mínimo, máximo, cuartiles) para las variables numéricas del dataset, principalmente `Edad`.

---

## Paso 6 – Datos Duplicados y Nulos

```python
# Verificación de duplicados
dataUy.duplicated().sum()

# Porcentaje de nulos por columna
print(dataUy.isnull().sum() * 100 / len(dataUy))
```

---

## Paso 7 – Análisis Exploratorio y Visualización

**Script**: `src/EntregaFinal.py`

Se carga el dataset preprocesado y se generan visualizaciones para cada variable de interés. Todos los gráficos utilizan paletas compatibles con daltonismo (`seaborn colorblind`).

### Carga del Dataset Preprocesado

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv('preprocesamiento_siniestros2022.csv')
```

### Visualizaciones Generadas

| # | Variable | Tipo de Gráfico | Descripción |
|---|---|---|---|
| 1 | `Edad` | Histograma + KDE | Distribución de la edad de los involucrados |
| 2 | `Edad` | Boxplot | Diagrama de caja de la variable edad |
| 3 | `Rol` | Barras (countplot) | Frecuencia por rol (conductor, pasajero, peatón) |
| 4 | `Rol` | Gráfico circular | Proporción de cada rol sobre el total |
| 5 | `Tipo_de_resultado` | Barras (countplot) | Distribución por tipo de resultado |
| 6 | `Tipo_de_siniestro` | Barras (countplot) | Distribución por tipo de siniestro |
| 7 | `Dia_de_la_semana` | Barras (countplot) | Siniestros por día de la semana |
| 8 | `Sexo` | Barras (countplot) | Distribución por sexo |
| 9 | `Sexo` | Gráfico de dona | Proporción por sexo |
| 10 | `Tipo_de_Vehiculo` | Barras (countplot) | Distribución por tipo de vehículo |
| 11 | `Momento_dia` | Barras (countplot) | Distribución por momento del día |
| 12 | `Hora_pico` | Barras (countplot) | Siniestros en hora pico vs. fuera de hora pico |
| 13 | `Hora_pico` | Gráfico circular | Proporción de siniestros en hora pico |

---

## Cómo Ejecutar el Proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/geramargonzalez/UTEC-SiniestrosAnalisis.git
cd UTEC-SiniestrosAnalisis
```

### 2. Instalar dependencias

```bash
pip install pandas numpy matplotlib seaborn plotly
```

### 3. Ejecutar el preprocesamiento

```bash
python src/SiniestrosDATABASE.py
```

> Esto descargará el dataset original, lo limpiará y generará el archivo `preprocesamiento_siniestros2022.csv` en el directorio de trabajo.

### 4. Ejecutar el análisis y visualizaciones

Antes de ejecutar, editar la variable `file_path` en `src/EntregaFinal.py` para que apunte al archivo generado en el paso anterior:

```python
file_path = "preprocesamiento_siniestros2022.csv"
```

Luego ejecutar:

```bash
python src/EntregaFinal.py
```

> Se generarán los 13 gráficos detallados en el Paso 7.

---

## Tecnologías Utilizadas

| Tecnología | Versión recomendada | Uso |
|---|---|---|
| Python | 3.8+ | Lenguaje principal |
| Pandas | ≥1.5 | Manipulación y análisis de datos |
| NumPy | ≥1.23 | Operaciones numéricas |
| Matplotlib | ≥3.6 | Visualizaciones estáticas |
| Seaborn | ≥0.12 | Visualizaciones estadísticas |
| Plotly Express | ≥5.0 | Gráficos interactivos |

---

*Proyecto desarrollado por el equipo de UTEC Python – 2022/2023.*
