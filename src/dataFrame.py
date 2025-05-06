# Se importa la librería
import pandas as pd
import numpy as np


datos = {'nombre':['María', 'Luis', 'Carmen', 'Antonio'], 'edad':[18, 22, 20, 21],
         'grado':['Economía', 'Medicina', 'Arquitectura', 'Economía'],
         'correo':['maria@gmail.com', 'luis@yahoo.es', 'carmen@gmail.com', 'antonio@gmail.com']}

df = pd.DataFrame(datos)
df.head()
print(df)

# DataFrame(data=listas, index=filas, columns=columnas, dtype=tipos)
# Si las listas anidadas en listas no tienen el mismo tamaño, las listas menores se rellenan con valores NaN.
df = pd.DataFrame([['María', 18], ['Luis', 22], ['Carmen', 20]], columns=['Nombre', 'Edad'])
print(df)

# DataFrame(data=array, index=filas, columns=columnas, dtype=tipo)
df = pd.DataFrame(np.random.randn(4, 3), columns=['a', 'b', 'c'])
print(df)

# Dependiendo del tipo de fichero, existen distintas funciones para importar un DataFrame desde un fichero.
# read_csv(fichero.csv, sep=separador, header=n, index_col=m, na_values=no-validos, decimal=separador-decimal)
# read_excel(fichero.xlsx, sheet_name=hoja, header=n, index_col=m, na_values=no-validos, decimal=separador-decimal)

df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesteroles.csv', sep=';', decimal=',')
print(df.head())

#Exportación de ficheros

#to_csv(fichero.csv, sep=separador, header=n, index_col=m, na_values=no-validos, decimal=separador-decimal)
#to_excel(fichero.xlsx, sheet_name=hoja, header=n, index_col=m, na_values=no-validos, decimal=separador-decimal)

# Importando datos csv
df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')

#info 
print(df.info())

 # Devuelve una tupla con el número de filas y columnas del DataFrame
print(df.shape)

# df.size devuelve el número de elementos del DataFrame
print(df.size)

#df.columns devuelve una lista con los nombres de las columnas del DataFrame
print(df.columns)

#df.index devuelve una lista con los nombres de los índices del DataFrame
print(df.index)

#len(df) devuelve el número de filas del DataFrame
print(len(df))

#df.dtypes devuelve una serie con los tipos de datos de cada columna del DataFrame
print(df.dtypes)

#Renombrar los nombres de las filas y columnas
df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
print(df.rename(columns={'nombre':'nombre y apellidos', 'altura':'estatura'}, index={0:1000, 1:1001, 2:1002}))

df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
print(df.set_index("nombre").head(14))

print(df.iloc[1, 3])

print(df.iloc[1, :3])

print(df.iloc[:4])