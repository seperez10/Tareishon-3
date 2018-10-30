import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
####Punto 1#####
### En primer lugar se van a tomar los datos del dataframe y los normalizaremos 
nd=31.0
cl= np.arange(0,nd+1)
#Ordenamos los datos de WDBC.dat en el dataframe para poder leerlos, utilizaremos pandas en esto ya que nos ayuda a evitar los datos que no sean numeros (nan)
data= pd.read_csv('WDBC.dat',names=cl)
#Borraremos la primera columna de los datos para facilitar el trabajo del archivo
data.drop(data.columns[[0]], axis=1, inplace=True)

