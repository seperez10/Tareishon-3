import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
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
#Vamos a realizar la transformada de fourier de los datos de signal.dat con la implementacion propia tal como lo dice el enunciado de la tarea
def TF(dt):
	gk=dt
	N=len(gk)
	dft=[]
	for n in range (0,N):
		contador=0.0
		for k in range (0,N):
			contador += (gk[k])*(np.exp(-2j*np.pi*k*n/N))
		dft.append(contador)
	return np.asarray(dft)
FT_sg=TF(y_sg)
N= len(FT_sg)
dt=0.0001
####Aqui realizamos el bono de los 3 puntos de la implementacion de la frecuencia de numpy
def freq(N,dt):
	f=np.zeros(N)
	if(N%2==0):
		f[int(N/2)]=-(N/2)
		for i in range(1,int(N/2)):
			f[i]
		for i in range(1,int(N/2)):
			f[-i]=-i
	return f/(N*dt)
Freq_sg=freq(N,dt)
######Cuarto punto#####
plt.plot(abs(Freq_sg),abs(FT_sg),label='Transf. de Fourier')
plt.legend()
plt.xlabel(r'$Frecuancias[Hz]$')
plt.ylabel(r'$Amplitud$')
plt.title('Transformada de Fourier de signal.dat')
plt.savefig('PerezSantiago_TF.pdf')
plt.close()

######Quinto punto####
##tomamos la frecuencias principales del signal.dat
ii=np.argmax(FT_sg)
Freq_sg=abs(Freq_sg)
maxfreq=Freq_sg[ii]
print('Las Frecuencias pricipales son',maxfreq,'Hz,',Freq_sg[501],'Hz y ',Freq_sg[506],'Hz')
#######Sexto punto##########
#realizamos el filtro pasabajos aca
def LPFilter(ft,freq):
	frt=ft.copy()
	freq_c=1000
	frt[abs(freq)>freq_c]=0
	return frt

FT_LPF=LPFilter(FT_sg,Freq_sg)
FIT_sg=np.fft.ifft(FT_LPF)
plt.plot(t_sg,FIT_sg.real,label='Datos con filtro')
plt.title('Datos de Signal.dat')
plt.xlabel(r'$y$')
plt.ylabel(r'$Y$')
plt.legend()
plt.savefig('PerezSantiago_signal.pdf')
######Septimo punto#####
#Ahora realizamos Fourier de los datos incompletos.dat
t_icp=datos_incompletos[:,0]
y_icp=datos_incompletos[:,1]
plt.scatter(t_icp,y_icp,label='Datos de incompletos.dat ',marker='.')
plt.title('Datos de Incompletos.dat')
plt.xlabel(r'$t$')
plt.ylabel(r'$Y$')
plt.legend()
plt.xlim([0.01,0.014])
plt.savefig('Figura_de_demostracion.pdf')
plt.close()
print('Realizando aparte un plot de los datos de incompletos.dat, se observa una disconti discontinuidades de los datos entre los tiempos 0.0115 y 0.0125 (Ver Figura_de_demostracion.pdf).')

####Octavo punto########
##Interpolacion cuadratica y cubica
inter_qd= interpolate.interp1d(t_icp,y_icp,kind='quadratic',fill_value="extrapolate")
inter_cb= interpolate.interp1d(t_icp,y_icp,kind='cubic',fill_value="extrapolate")
nwt_icp=np.linspace(0,0.029,512)
nwy_icp_qd=inter_qd(nwt_icp)
nwy_icp_cb=inter_cb(nwt_icp)

#Realizamos fourier aca

FT_icp_qd=DFT(nwy_icp_qd)
FT_icp_cb=DFT(nwy_icp_cb)
Freq_icp=freq(N,dt)

####Noveno punto####
####LAs mil graficas de los datos que tiene signal e incompletos ya interpolados





