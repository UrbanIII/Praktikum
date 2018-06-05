# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt
import math

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
data = np.loadtxt("serienkreis")
omega = np.array(data[:,0])
omega_err = math.pi; # PLATZHALTER
phase = np.array(data[:,3])
phase_err = np.array(data[:,4])

plt.errorbar(omega,phase,xerr = omega_err,yerr=phase_err,fmt="g.",label="Messwerte",ecolor="red")
plt.xlabel(r'Kreisfrequenz $\omega$ $[\mathrm{s}^{-1}]$')
plt.ylabel(r'Phasenverschiebung $\varphi$ in Grad')

Widerstand = 100 #Geraten
Kapazitaet = 1.8*10**-6
Resonanzfrequenz = 1190
Induktivitaet = 1/(Kapazitaet*Resonanzfrequenz**2)

def f(x,a,b): #Fitfunktion
    return np.arctan((x*a-1.0/(x*b)))/(2*math.pi)*360

params, pcov = opt.curve_fit(f, omega, phase, p0 = [Induktivitaet/Widerstand,Kapazitaet*Widerstand]) #Wild guess for L
perr = np.sqrt(np.diag(pcov))
print 'A:\t', params[0], '+/- ',perr[0]
print 'B:\t', params[1], '+/-', perr[1]
Resonanzfrequenz = math.sqrt(1/(params[0]*params[1]))
Resonanzfrequenz_err = math.sqrt((perr[0]/(2*params[1]**0.5*params[0]**1.5))**2+(perr[1]/(2*params[0]**0.5*params[1]**1.5))**2)
print 'Resonanzfrequenz:\t', Resonanzfrequenz, '+/-', Resonanzfrequenz_err

#clean up the values
def clean(val, err):
        err_pow = math.floor(math.log(err,10)) # Potenz des Fehlers finden
        err = math.ceil(err/10**err_pow)*10**err_pow
        err_pow = math.floor(math.log(err,10)) # neue Fehlerpotenz (kann sich durch Aufrunden ändern)
        val_pow = math.floor(math.log(abs(val),10))
        pow = max(val_pow, err_pow)
        fmt = '1.'+str(int(pow-err_pow))+'f' #Format-String
        if val_pow == 0:
                return '('+format(val,fmt)+' $\pm$ '+format(err/10**pow,fmt)+')'
        else:
            return '('+format(val/10**pow,fmt)+' $\pm$ '+format(err/10**pow,fmt)+')$\cdot 10^{'+str(int(pow))+'}$'

x_axis = np.linspace(omega[0],omega[4],100)
plt.plot(x_axis, f(x_axis,params[0],params[1]),label='arctan('+clean(params[0],perr[0])+'s $\cdot \omega$\n$-1/($'+clean(params[1],perr[1])+'s$\cdot \omega$))')
plt.legend(loc='lower right')

fig = plt.gcf()
plt.show()
fig.savefig('3.eps')
