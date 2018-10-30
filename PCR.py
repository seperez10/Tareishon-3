import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
####Punto 1#####
### En primer lugar se van a tomar los datos del dataframe y los normalizaremos 
nd=31.0
cl= np.arange(0,nd+1)
#Ordenamos los datos de WDBC.dat en el dataframe para poder leerlos, utilizaremos pandas en esto ya que nos ayuda a evitar los datos que no sean numeros (nan)
datos= pd.read_csv('WDBC.dat',names=cl)
#Borraremos la primera columna de los datos para facilitar el trabajo del archivo
datos.drop(datos.columns[[0]], axis=1, inplace=True)
#Obtenemos los valores de los datos
datos = datos.values
# Se crean dos matrices con la misma longitud de los datos 
columnasdat= len(data[0])
filasdat= len(data[:,0])
# los datos de la parte de diagnostico ya que aparecen en letras las volvemos ceros y unos (cuando es maligno es 1 y cuando es beningno es 0)
for i in range(filasdat):
	if(datos[i,0]=='M'):
		datos[i,0]=1
	else:
		datos[i,0]=0

#Creamos una matriz de ceros con las filas y las columnas
matriz0=np.zeros(filasdat,columnasdat)
#Aqui realizamos la normalizacion de los datos 
for i in range(0,columnasdat):
	matriz[:,i]= (datos[:,i]-datos[:,i].mean())/ (datos[i].std())


