from __future__ import division
from math import*
import matplotlib.pyplot as plt
r=input()
ctr=0
ax = plt.gca()
ax.add_patch(plt.Circle((0,0),radius=r,facecolor=(.7,.7,.7),edgecolor='black'))
for n in range(-r-1,r+1):
    xn=n
    for m in range(-r-1,r+1):
        ym=m
        if(xn**2+ym**2<=(r+3/4)**2):
            ctr=ctr+1
            ax.add_patch(plt.Rectangle((xn-1/2,ym-1/2),1,1,facecolor=(.7,.5,.5,.5),edgecolor=(.2,.1,.1,.5)))
            ax.text(xn,ym,str(ctr),fontsize=12,horizontalalignment='center',verticalalignment='center',color='black')
plt.xlim([-r-1,r+1])
plt.ylim([-r-1,r+1])
plt.axes().set_aspect('equal')
plt.savefig('uputa.pdf')
plt.show()
