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

data = np.loadtxt("plt1.txt")
z2 = data[:,0] #Spannung
w2 = data[:,1] #Feld

data2 = np.loadtxt("plt1_f.txt")
zerr = data2[:,0]
werr = data2[:,1]


plt.title(r'Impendanzquadrat $Z^2$ gegen Kreisfrequenzquadrat $f^2$')
plt.ylabel(r'Quadrat der Impendanz $Z^2$ in $10^6$ [$\frac{V^2}{A^2}$]')
plt.xlabel(r'Quadrat der Kreisfrequenz $f^2$ in $10^7$ [$s^{-2}$]')

def f(x,a,b): #Fitfunktion, x-Achsen-Wert immer zuerst!
    return a*x+b

#def scaled_f(x,a,b):
#    return np.exp(b)*x**a

#Anfangswerte
a = 0.15
b = 10000

params, pcov = opt.curve_fit(f, w2, z2)
perr = np.sqrt(np.diag(pcov))
print ('Steigung:\t', params[0], '\t+/-',perr[0])
print ('y-Abschnitt:\t', params[1], '\t\t+/-', perr[1])

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


x_axis = np.linspace(w2[0],w2[-1],num=100)
plt.errorbar(w2,z2,xerr = werr,yerr=zerr,fmt="ro",label="Messwerte")
plt.plot(x_axis, f(x_axis,params[0],params[1]), label=clean(params[0],perr[0])+r'$\,V^2 \cdot s^2 \cdot A^{-2} \cdot f^2 +$'+clean(params[1],perr[1])+r'$V^2 \cdot A^{-2}$', color='c')

plt.legend(framealpha=0.5)
plt.yticks(np.arange(0,1500000,200000),('0','0.2','0.4','0.6','0.8','1.0','1.2','1.4'))

fig = plt.gcf()
plt.show()
fig.savefig('ausw1.pdf')

#a = 0.152992207548             = 
#Fehler a = 0.000714947835845   = 
#b = 5297.91810999              = 
#Fehler b = 3349.55722719       = 