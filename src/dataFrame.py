# Se importa la librería
import pandas as pd
import numpy as np


datos = {'nombre':['María', 'Luis', 'Carmen', 'Antonio'], 'edad':[18, 22, 20, 21],
         'grado':['Economía', 'Medicina', 'Arquitectura', 'Economía'],
         'correo':['maria@gmail.com', 'luis@yahoo.es', 'carmen@gmail.com', 'antonio@gmail.com']}

df = pd.DataFrame(datos)
df.head()