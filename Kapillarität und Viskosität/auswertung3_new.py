# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

golden_ratio = (1+np.sqrt(5))/2
width = 6.202 #Measured in Latex! (inches)
height = width/golden_ratio #This is supposed to look really nice.

settings = {
    'figure.figsize': [width,height],
    'font.family': 'serif',
    'figure.autolayout': True,
    'figure.titlesize': 14,
    'axes.titlesize': 12,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10
}

plt.rcParams.update(settings)
#print plt.rcParams
data = np.loadtxt("data2b")
t = data[:,0]
h = data[:,1]
terr = 0.005*t+0.3 #0.3 = Schätzwert, Rest siehe Praktikumsbuch
herr = 0.2 #Schätzwert in cm
lnerr = np.sqrt((herr/h)**2+(herr/h[0])**2) #Gauß

plt.title('Ausfluss des Wassers durch die dünnste Kapillare')
plt.errorbar(t,np.log(h/h[0]),xerr = terr,yerr=lnerr,fmt="go",label="Messwerte",ecolor="red")
plt.xlabel(r'$t$ [s]')
plt.ylabel(r'$\ln\left(\frac{h(t)}{h_0}\right)$')

def f(x,a,b): #Fitfunktion
    return a*x+b

params, pcov = opt.curve_fit(f, t, np.log(h/h[0])) #log = ln
perr = np.sqrt(np.diag(pcov))
print 'Anstieg:\t', params[0], '+/- ',perr[0]
print 'Achsenabschnitt:\t', params[1], '+/-', perr[1]

x_axis = np.linspace(0,t[-1],100)
plt.plot(x_axis, f(x_axis,params[0],params[1]),label=r'(-1.356 $\pm$ 0.004)$\cdot 10^{-3}\,\mathrm{s}^{-1}\cdot t\,-(5\pm8)\cdot 10^{-4}$')
plt.legend(loc='upper right')

fig = plt.gcf()
plt.show()
fig.savefig('auswertung3.eps')
