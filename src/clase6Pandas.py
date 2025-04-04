#pANDAS 
import pandas as pd
import numpy as np

# Creando un objeto Serie pasando una lista de elementos string
s = pd.Series(['Matemáticas', 'Historia', 'Economía', 'Programación', 'Inglés'], dtype='string')
print(s)

# Creando un objeto Serie pasando una lista de valores y usando numpy
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

print(type(s[3]))

# Creando un objeto Serie pasando una lista de valores
s2 = pd.Series([1, 3, 5, "nan", 6, 8])
print(s2)

# Creando un objeto Serie pasando un diccionario
s = pd.Series({'Matemáticas': 6.0,  'Economía': 4.5, 'Programación': 8.5})
print(s)

#Usando atributos de una serie
s = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print('Size: ', s.size) 

print('Index: ', s.index)

print('dtype: ', s.dtype)


# Accediendo a elementos de un objeto serie
s = pd.Series({'Matemáticas': 6.0,  'Economía': 4.5, 'Programación': 8.5})

print('Matematica: ', s['Matemáticas'])

print('Iterator: ', s[0:3])

print('Two elements: ', s[['Programación', 'Matemáticas']])


#Las siguientes funciones permiten resumir varios aspectos de una serie:

#Devuelve el número de elementos que no son nulos ni NaN en la serie s
s.count()

#Devuelve la suma de los datos de la serie s cuando los datos son de un tipo numérico, o la concatenación de ellos cuando son del tipo cadena str.
s.sum()

#Devuelve una serie con la suma acumulada de los datos de la serie s cuando los datos son de un tipo numérico
s.cumsum()

#Devuelve una serie con la frecuencia (número de repeticiones) de cada valor de la serie 
s.value_counts()

#Devuelve el menor de los datos de la serie 
s.min()

#Devuelve el mayor de los datos de la serie 
s.max()

#Devuelve la media de los datos de la serie s cuando los datos son de un tipo numérico
s.mean()
 #Devuelve la varianza de los datos de la serie s cuando los datos son de un tipo numérico
s.var()
 #Devuelve la desviación típica de los datos de la serie s cuando los datos son de un tipo numérico
s.std()
 #Devuelve una serie con un resumen descriptivo que incluye el número de datos, su suma, el mínimo, el máximo, la media, la desviación típica y los cuartiles
s.describe()

s = pd.Series([1, 1, 1, 1, 2, 2, 2, 3, 3, 4])
 # Tamaño muestral
print(s.count()) 

#Aplicar operaciones a una serie print()

s = pd.Series([1, 2, 3, 4]) #Multiplicación con int
print('Multiplicacion ',s * 2)

#Modulo
print('Modulo ', s % 2)

 #Multiplicación con string
s = pd.Series(['a', 'b', 'c']) 
print('Multiplicacion ', s * 5)


#Aplicar funciones a una serie

from math import log

#Aplicando la función log a la serie
s = pd.Series([1, 2, 3, 4]) 
s.apply(log)

# Aplicando funciones a la serie con datos tipo string
s = pd.Series(['a', 'b', 'c']) 
s.apply(str.upper)

#s[condicion]: Devuelve una serie con los elementos de la serie s que se corresponden con el valor True de la lista booleana condicion. 
#condicion debe ser una lista de valores booleanos de la misma longitud que la serie.
s = pd.Series({'Matemáticas': 6.0,  'Economía': 4.5, 'Programación': 8.5})
print(s[s > 5])

#Ordenar una serie
s = pd.Series({'Matemáticas': 6.0,  'Economía': 4.5, 'Programación': 8.5})
print(s.sort_values(ascending=False))
print(s.sort_index(ascending = True))

#Eliminar los datos desconocidos en una serie
s = pd.Series(['a', 'b', None, 'c', np.nan,  'd'])
#s.dropna(): Elimina los datos desconocidos o nulos de la serie s.
s.dropna()