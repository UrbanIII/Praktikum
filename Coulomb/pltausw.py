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
    'legend.fontsize': 8,
    #'xtick.labelsize': 10,
    #'ytick.labelsize': 10
}

plt.rcParams.update(settings)

data = np.loadtxt("pltausw2_w.txt")
m = data[:,0] #Spannung
r = data[:,1] #Feld

data2 = np.loadtxt("pltausw2_f.txt")
merr = data2[:,0]
rerr = data2[:,1]


plt.title(r'Steigung $m$ gegen Abstand $r$ von Kugel und Elektrofeldmeter')
plt.ylabel(r'Anstieg $m$ [$\frac{1}{m}$]')
plt.xlabel(r'Abstand $r$ [m]')

def f(x,a,b): #Fitfunktion, x-Achsen-Wert immer zuerst!
    return a*x+b

def scaled_f(x,a,b):
    return np.exp(b)*x**a

params, pcov = opt.curve_fit(f, np.log(r), np.log(m))
perr = np.sqrt(np.diag(pcov))
print ('Steigung:\t', params[0], '+/- ',perr[0])
print ('y-Abschnitt:\t', params[1], '+/-', perr[1])

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

x_axis = np.linspace(r[0],r[-1],num=100)
plt.xscale('log')
plt.yscale('log')
plt.errorbar(r,m,xerr = rerr,yerr=merr,fmt="bo",label="Daten")
plt.plot(x_axis, scaled_f(x_axis,params[0],params[1]), label=clean(params[0],perr[0])+r'$\,EINHEIT \cdot GRÖSSE +$'+clean(params[1],perr[1])+r'm', color='b')

plt.legend(framealpha=0.5)

fig = plt.gcf()
plt.show()
fig.savefig('ausw2.pdf')
