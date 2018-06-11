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
U = np.array(data[:,1])
U_err = 0.005 # halber Skalenteil
I = data[:,2]
I_err = np.array([])

for i in range(len(I)):
    if I[i]<40:
        # I_err = I_err + [0.005]
        I_err = np.concatenate((I_err,[0.005]))
    else:
        # I_err = I_err + [0.05]
        I_err = np.concatenate((I_err,[0.05]))

I = I/1000 #Umrechnung in Ampère
I_err = I_err /1000
Z = U/I
Z_err = np.sqrt((U_err/I)**2+(U/I**2*I_err)**2)

plt.errorbar(omega,Z,xerr = omega_err,yerr=Z_err,fmt="g.",label="Messwerte",ecolor="red")
plt.xlabel(r'Kreisfrequenz $\omega$ $[\mathrm{s}^{-1}]$')
plt.ylabel(r'Gesamte Impedanz $Z_0 = \frac{U}{I}$ $[\Omega]$')

# def f(x,r,l,c): #Fitfunktion
#     return np.sqrt(r**2+(x*l-1/x/c)**2)

# params, pcov = opt.curve_fit(f, omega, Z) #Man sollte wahrscheinlich p0 angeben
# perr = np.sqrt(np.diag(pcov))
# print 'Widerstand:\t', params[0], '+/- ',perr[0]
# print 'Kapazität:\t', params[1], '+/-', perr[1]
# print 'Induktivität:\t', params[2], '+/-', perr[2]

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

# x_axis = np.linspace(omega[0],omega[-1],100)
# plt.plot(x_axis, f(x_axis,params[0],params[1],params[2]),label=clean(params[0],perr[0])+'$\cdot R+$'+clean(params[1],perr[1]))

plt.axvline(x=1190, label='abgelesenes Minimum')
plt.axhline(y=91)
plt.legend(loc='upper right')
fig = plt.gcf()
plt.show()
fig.savefig('2.eps')

# Zoom
plt.errorbar(omega,Z,xerr = omega_err,yerr=Z_err,fmt="g.",label="Messwerte",ecolor="red")
plt.xlabel(r'Kreisfrequenz $\omega$ $[\mathrm{s}^{-1}]$')
plt.ylabel(r'Gesamte Impedanz $Z_0 = \frac{U}{I}$ $[\Omega]$')
plt.axis([1120,1265,90,105])
plt.axvline(x=1190, label='abgelesenes Minimum')
plt.axhline(y=91)
plt.legend(loc='center right')
fig = plt.gcf()
plt.show()
fig.savefig('2_zoom.eps')
