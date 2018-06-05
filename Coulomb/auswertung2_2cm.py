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
data = np.loadtxt("data3_2cm")
U = [1000,2000,3000,4000,5000] # in Volt
E = data*1000
U_err = 0.05 * 1000 # Halber Skalenteil
E_err = 0.002 + 0.3*E #Schätzwert

#plt.title('Zusammenhang zwischen Feldstärke des elektrischen Felds und Ladespannung für Kugel mit 2cm Radius')
plt.errorbar(U,E,xerr = U_err,yerr=E_err,fmt="go",label="Messwerte",ecolor="red")
plt.xlabel(r'Ladespannung $U$ [V]')
plt.ylabel(r'Feldstärke $E$ [V/m]')

def f(x,a,b): #Fitfunktion
    return a*x+b

params, pcov = opt.curve_fit(f, U, E) #log = ln
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

x_axis = np.linspace(0,U[-1],100)
#plt.plot(x_axis, f(x_axis,params[0],params[1]),label=r'(1,2 $\pm$ 0,3)$\cdot 10^{2}\,\mathrm{m}^{-1}\cdot U\,-(9\pm10)\cdot 10^{1}$ V/m')
plt.plot(x_axis, f(x_axis,params[0],params[1]),label=clean(params[0],perr[0])+'$\,\mathrm{m}^{-1}\cdot U\,+$'+clean(params[1],perr[1])+' V/m')
plt.legend(loc='upper left')

fig = plt.gcf()
plt.show()
fig.savefig('auswertung2_2cm.eps')
