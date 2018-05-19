# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

data = np.loadtxt("data2b")
t = data[:,0]
h = data[:,1]

plt.yscale('log')
#plt.axis([-10,t[-1]+10,10**-0.3,10**0.05])
#plt.yticks([10**-0.3,10**-0.2,10**-0.21,1],['10**-0.3','10**-0.2','10**-0.1','1'])
#plt.yticks([10**-0.3,10**-0.2,10**-0.1,1],[r'$10^{-0.3}$','10**-0.2','10**-0.1','1'])
plt.title('Ausfluss des Wassers durch die dünnste Kapillare')
#plt.errorbar(t,h,xerr=0.3,yerr=0.2,fmt="go",label="Messwerte",ecolor="red")
plt.plot(t,h/h[0],'gx',label='Messwerte')
plt.xlabel(r'$t$ [s]')
plt.ylabel(r'$\ln\left(\frac{h(t)}{h_0}\right)$')

def f(x,a):
    return np.exp(a*x)

estimate = np.pi*1000*9.81*(0.0004)**4/(8*8.9*10**-4*0.23*(10**-6/0.05))

params, pcov = opt.curve_fit(f, t, h/h[0], p0 = estimate) #log = ln
perr = np.sqrt(np.diag(pcov))
print 'Anstieg:\t', params[0], '+/- ',perr[0],

x_axis = np.linspace(0,t[-1],100)
plt.plot(np.linspace(0,t[-1],100), f(np.linspace(0,t[-1],100),params[0]),label='Fit')

plt.legend(loc='lower right')

fig = plt.gcf()
plt.show()
fig.savefig('auswertung3.eps')
