import numpy as np
import matplotlib.pyplot as plt

######Primer punto#####
#Simplemente leemos los datos del signal.dat
datos_senal= np.genfromtxt('signal.dat', usecols=[0,2])
datos_incompletos= np.genfromtxt('incompletos.dat', usecols=[0,2])

#####Segundo punto#####
# Aqui graficaremos los datos delsignal.dat
t_sg=datos_senal[:,0]
y_sg=datos_senal[:,1]
plt.plot(t_sg,y_sg,linestyle=':',label='datos')
plt.title('datos del signal.dat')
plt.xlabel(r'$y$')
plt.ylabel(r'$Y$')
plt.legend()
plt.savefig('PerezSantiago_signal.pdf')
plt.close()

#######Tercer punto#####

