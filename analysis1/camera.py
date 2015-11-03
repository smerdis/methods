import numpy as np

cam1d = np.loadtxt('camera.txt')
cr = cam1d.reshape(512,512)
cr = cr.T
plt.imshow(cr,plt.cm.gray)
T = 0.15
plt.imshow(cr>T,plt.cm.gray)
