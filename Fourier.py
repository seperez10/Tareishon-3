import numpy as np
import matplotlib.pyplot as plt

######Primer punto#####
#Simplemente leemos los datos del signal.dat
datos_senal= np.genfromtxt('signal.dat', usecols=[0,2])
datos_incompletos= np.genfromtxt('incompletos.dat', usecols=[0,2])

#####Segundo punto#####
# Aqui graficaremos los datos delsignal.dat
t_sg=datos_senal[:,0]

