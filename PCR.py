import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
#####Todo se sube a github cuando este corriendo bien###
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
columnasdat= len(datos[0])
filasdat= len(datos[:,0])
# los datos de la parte de diagnostico ya que aparecen en letras las volvemos ceros y unos (cuando es maligno es 1 y cuando es beningno es 0)
for i in range(filasdat):
	if(datos[i,0]=='M'):
		datos[i,0]=1
	else:
		datos[i,0]=0

#Creamos una matriz de ceros con las filas y las columnas
matriz0=np.zeros((filasdat,columnasdat))
#Aqui realizamos la normalizacion de los datos 
for i in range(0,columnasdat):
	matriz0[:,i]= (datos[:,i]-datos[:,i].mean())/ (datos[i].std())

######Segundo Punto#####
#Aqui implementaremos la matriz de covarianza 
#En primer lugar tenemos que transponer los nuevos datos ya normalizados 
matriz0 = matriz0.T
M= len(matriz0[0,:])
matrizcov= np.zeros((columnasdat,columnasdat))
for i in range(0,columnasdat):
	for j in range(0,columnasdat):
		matrizcov[i,j]= sum((matriz0[i,:]-matriz0[i,:].mean())*(matriz0[j,:]-matriz0[j,:].mean()))/(M-1)
####Tercer punto####

####Vamos a imprimir los vectores y los valores propios de los vectores
valores, vectores= np.linalg.eig(matrizcov)
#Imprimimos el mensaje del autovector correspondiente a cada autovalor
for i in range(columnasdat):
	print("El autovector [], tiene autovalor []".format(vectors[:,i],values[i]))
print('\n')

#####Cuarto punto#####
#Los parametros mas importantes son
total=np.sum(values)
percent=values*100/total
for i in range(columns):
    print('El autovalor {}, describe {}% de los datos'.format(values[i],percent[i]))
maxpercent=percent[0]+percent[1]+percent[2]
print('\n')
print('Las primeras 3 componentes describen el {}% de los datos. Por lo tanto, estos tres primeros parametros son los mas importantes'.format(maxpercent))
print('\n')












