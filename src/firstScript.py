
# Librerias a utilzar
import pandas as pd
import numpy as np


dataUy=pd.read_csv('https://ckan-data.montevideo.gub.uy/dataset/13c5b4a6-ff33-454f-8e9f-c3871052f464/resource/e2beee51-f90b-4712-aec7-a336784a23cb/download/automaticas_23.csv')
dataUy.head()

#Conociendo el conjunto de datos
dataUy.info()

dataUy['Hora'] = pd.to_datetime(dataUy['Hora'], format=' %H')
dataUy['Hora'].tail()

# Visualización de las columnas (Variables)
dataUy.columns

#Tamaño del conjunto de datos
print(dataUy.shape)

#Número de observaciones
len(dataUy)

#Identificación y suma de datos nulos
dataUy.isnull().sum()


#Identificación e identificación de datos nulos en porcentaje
print(dataUy.isnull().sum()*100/len(dataUy))

# Identificación de datos duplicados
dataUy.duplicated().sum()

#Principales estadísticos
dataUy.describe()
