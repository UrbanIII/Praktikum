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
data = np.loadtxt("data_slopes")
R = [0.01,0.02,0.06] # Radius der Kugeln in m
m = data[:,0]
m_err = data[:,1]
r = 0.25 # Abstand Kugel - Messgerät in m
r_err = 0.002 # Schätzwert in m
mrsq = m*r**2
mrsq_err = np.sqrt((r**2*m_err)**2+(2*m*r*r_err)**2) # Gauß

plt.errorbar(R,mrsq,xerr = 0,yerr=mrsq_err,fmt="go",label="Messwerte",ecolor="red")
plt.xlabel(r'Kugelradius $R$ [m]')
plt.ylabel(r'$mr^2$ [m]')

def f(x,a,b): #Fitfunktion
    return a*x+b

params, pcov = opt.curve_fit(f, R, mrsq) #log = ln
perr = np.sqrt(np.diag(pcov))
print 'Anstieg:\t', params[0], '+/- ',perr[0]
print 'Achsenabschnitt:\t', params[1], '+/-', perr[1]

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

print clean(123.45,21.9)

x_axis = np.linspace(0,R[-1],100)
plt.plot(x_axis, f(x_axis,params[0],params[1]),label=clean(params[0],perr[0])+'$\cdot R+$'+clean(params[1],perr[1]))
plt.legend(loc='upper left')

fig = plt.gcf()
plt.show()
fig.savefig('auswertung2_advanced.eps')
