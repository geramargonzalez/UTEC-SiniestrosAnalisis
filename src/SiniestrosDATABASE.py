
# Librerias a utilzar
import pandas as pd
import numpy as np

#1. Importa al noteboook el conjunto de datos seleccionado.

#Importamos la base de datos del catálogo de datos de Uruguay
dataUy=pd.read_csv(' https://ckan-data.montevideo.gub.uy/dataset/d8b39296-5fcf-4a8e-ac9f-d02a24698b97/resource/f1157e84-9577-4d8f-b2f3-92c1d720ae93/download/siniestros2022.csv')
dataUy.head()

# 2. Realiza los pasos mediante las técnicas presentadas para evaluar la calidad de los datos. ¿Consideras que tienes datos de calidad?

#Renombramos las variables con el formato recomendado
def clean_column_name(col):
    # Cambiamos los nombres de las variables reemplazando espacios por _
    col = col.strip().replace(" ", "_")
    return col

# Aplicamos la función a los nombres de las columnas
dataUy.columns = [clean_column_name(col) for col in dataUy.columns]
print(dataUy.columns)


# Remplazamos las variables que contenian el caracter "�" por el correcto
dataUy.rename(columns={'Usa_cinturI�n': 'Usa_cinturon','DI�a_de_la_semana': 'Dia_de_la_semana'}, inplace=True)
print(dataUy.columns)

# Eliminamos los espacios de toda la base de datos
dataUy = dataUy.applymap(lambda x: x.strip() if isinstance(x, str) else x)

#VARIABLE NUMÉRICA
#Analizamos que los datos faltantes no aparecen como NaN ni como None, sino que dicen "SIN DATOS".
# Remplazamos el valor "SIN DATOS" de la variable "EDAD" por NaN, y convertimos a FLOAT
dataUy['Edad'] = dataUy['Edad'].replace('SIN DATOS',  np.nan) #En lugar de 0, reemplacé por nan
dataUy['Edad'] = dataUy['Edad'].astype(float)
dataUy['Edad'].head()


#VARIABLE DATE
#Convertimos las variables "FECHA" y "HORA" a date
dataUy['Fecha'] = pd.to_datetime(dataUy['Fecha'], format='mixed')
dataUy['Fecha'].tail()

dataUy['Hora'] = pd.to_datetime(dataUy['Hora'], format='%H').dt.time
dataUy['Hora'].head()

#Creamos una nueva variable apartir de la fecha y hora
dataUy['Fecha_Hora'] = dataUy.apply(lambda row: pd.Timestamp.combine(row['Fecha'], row['Hora']), axis=1)

print(dataUy[['Fecha', 'Hora', 'Fecha_Hora']].head())


#VARIABLES CATEGORICAS
#Remplazamos el valor "SIN DATOS" de las variables "Usa_casco", "Calle", "Localidad", "Tipo_de_Vehiculo", "Zona", "Usa_cinturon" por NONE
columns_to_replace = ['Usa_casco', 'Calle', 'Localidad', 'Tipo_de_Vehiculo', 'Zona','Usa_cinturon', 'Sexo']

for col in columns_to_replace:
    dataUy[col] = dataUy[col].replace('SIN DATOS', None)

# Verficamos que los cambios aplicados anteriormente se ejecutaron correctamente
dataUy.info()


#3. ¿Qué tamaño tiene el conjunto de datos a trabajar?

#Tamaño del conjunto de datos
print(dataUy.shape)
print('El conjunto de datos tiene 7.802 observaciones (filas) y 19 variables originales (columnas).')


#5. ¿Qué encontró relevante de los principales estadísticos?
dataUy.describe()


#6. ¿Tiene su conjunto de datos, datos duplicados?¿cuátos?
dataUy.duplicated().sum()


#Identificación y suma de datos nulos
#Calculamos el porcentaje que representan sobre el total
print(dataUy.isnull().sum()*100/len(dataUy))


#Identificamos en el paso anterior que las variables "Usa_cinturon" y "Usa_casco" tienen mas del 20% de datos nulos
#Por lo cual eliminamos de la base de datos dichas variables
dataUy = dataUy.drop(columns='Usa_cinturon')
dataUy = dataUy.drop(columns='Usa_casco')

#Verificamos que las variables no esten mas
print(dataUy.columns)


# VARIABLES CATEGORICAS
# Verificamos que las variables categoricas tengan los valores como lo dice la metadata
print(dataUy['Rol'].unique())  # Verificar los valores únicos de la variable "ROL", estan ok con la metadata

# Verificar los valores únicos de la variable "ZONA", estan ok con la metadata
print(dataUy['Zona'].unique())  

# Verificar los valores únicos de la variable "TIPO DE RESULTADO", estan ok con la metadata
print(dataUy['Tipo_de_resultado'].unique()) 

# Verificar los valores únicos de la variable "TIPO DE SINIESTRO", estan ok con la metadata pero hay un error tipografico
print(dataUy['Tipo_de_siniestro'].unique()) 

#Econtramos un error tipografico en la variable, lo modificamos
dataUy['Tipo_de_siniestro'] = dataUy['Tipo_de_siniestro'].replace('COLISION CON OBSTICULO EN CALZADA','COLISION CON OBSTACULO EN CALZADA')

#Comprobamos que se haya modificado correctamente
print(dataUy['Tipo_de_siniestro'].unique())

# Verificar los valores únicos de la variable "DIA DE LA SEMANA", estan ok con la metadata, pero hay un error tipografico
print(dataUy['Dia_de_la_semana'].unique())


#Encontramos un error tipografico en la variable, lo modificamos
dataUy['Dia_de_la_semana'] = dataUy['Dia_de_la_semana'].replace('SIBADO','SABADO')

#Comprobamos que se haya modificado correctamente
print(dataUy['Dia_de_la_semana'].unique())

# Verificar los valores únicos de la variable "SEXO", estan ok con la metadata
print(dataUy['Sexo'].unique()) 

# Verificar los valores únicos de la variable "TIPO DE VEHICULO", hay otros valoes adicionales a la metada
print(dataUy['Tipo_de_Vehiculo'].unique()) 


#Encontramos que la variable "TIPO DE VEHICULO", tiene mas opciones de los que nos dice la metada, dan mas informacion
#Dejamos laos nuevos valores que tiene sentido y remplazamos por OTRO el que no.
#Los nuevos valores son: CAMIONETA, MOTOCICLETA, CICLOMOTOR, TRICICLO
#Los valores remplazados por OTRO son: PEATON y CHAPA MATRICULA

dataUy['Tipo_de_Vehiculo'] = dataUy['Tipo_de_Vehiculo'].replace('PEATON','OTRO')
dataUy['Tipo_de_Vehiculo'] = dataUy['Tipo_de_Vehiculo'].replace('CHAPA MATRICULA','OTRO')

print(dataUy['Tipo_de_Vehiculo'].unique())