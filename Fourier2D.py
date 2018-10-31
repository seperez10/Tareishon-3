from scipy import fftpack
import numpy as np
import matplotlib.pyplot as plt

#####Primer punto######
####Almacenamos la imagen en un arreglo de numpy 
img = plt.imread('arbol.png')
######Segundo punto#####
#Graficamos la transformada sin el filtro
img_ft = fftpack.fft2(img, axes=(0, 1))
img_ft = fftpack.fftshift( img_ft )
ps=np.log10(np.abs(img_ft)**2)
fig = plt.figure(1, figsize=(9.5,9))
plt.imshow(ps,cmap='ocean')
bar=plt.colorbar()
bar.ax.set_ylabel('$\mathrm{Intensidad}$')
plt.title('Transformada de Fourier de la imagen sin filtro')
plt.xlabel(r'$X$')
plt.ylabel(r'$Y$')
plt.savefig('PerezSantiago_FT2D.pdf')
plt.close()
