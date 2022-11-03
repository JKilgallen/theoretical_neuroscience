import matplotlib.pyplot as plt
import numpy as np

lam=1.2 
ep0=1.0
X, Y = np.meshgrid(np.arange(0.05, 3, 0.01), np.arange(-2,2, 0.01))

ep=ep0*(np.exp(X/lam)-1)
a=-(180*(ep0+ep)*Y)/(lam*ep*np.pi)                      
a=a*(abs(a)<90)+90*(a>=90) - 90*(a<=-90)

K=8
Theta=np.pi/6
Phi=0;
s=np.cos(K*X*np.cos(Theta)+K*Y*np.sin(Theta)-Phi)
fig, axs = plt.subplots(1,2)
fig.set_figwidth(16)
fig.set_figheight(8)

axs[0].pcolor(X[0,:], Y[:, 0], s*(abs(a) < 90))
axs[0].set_title("Visual Cortex Activity")
axs[0].set_xlabel("X (cm)")
axs[0].set_ylabel("Y (cm)")
axs[1].contourf(ep*np.cos(a*2*np.pi/360),ep*np.sin(a*2*np.pi/360),s)
axs[1].set_title("Visual Space")
axs[1].set_xlabel("degrees")
axs[1].set_ylabel("degrees")
plt.show()