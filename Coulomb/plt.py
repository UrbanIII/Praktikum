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
    'figure.autolayout': False,
    'figure.titlesize': 14,
    'axes.titlesize': 12,
    'legend.fontsize': 10,
    #'xtick.labelsize': 10,
    #'ytick.labelsize': 10
}

plt.rcParams.update(settings)
#print plt.rcParams
#werte = []
werte = np.zeros([][])

for i in range(10) : # Sorry, bin an diese Variante gewöhnt
    data = np.loadtxt('plt'+str(i+1)+'.txt')
    #werte = werte + [data]


#werte = np.array(werte)
#print werte

plt.title('$E$ gegen $U_{B}$ fuer verschiedene $r$')
#plt.errorbar(U1,E1,xerr = U1err,yerr=E1err,fmt="bo",label="r=200mm")  #1

#Bezeichnungsarray für die label in plt.errorbar
bez = np.array([["r=200mm"],["r=210mm"],["r=222mm"],["r=236mm"],["r=253mm"],["r=274mm"],["r=302mm"],["r=340mm"],["r=397mm"],["r=500mm"]])

i = 0
print (i)
for i in range(1,10,1) :
	plt.errorbar(werte[(i-1),0],werte[(i-1),1],xerr = werte[(i-1),2],yerr = werte[(i-1),3],fmt="bo", label=bez[0,(i-1)])

'''
data = np.loadtxt("plt200.txt")
U1 = data[:,0] #Spannung
E1 = data[:,1] #Feld
U1err = 0.05*U1 #5% Spannungsfehler
E1err = E1/3 #

data = np.loadtxt("plt210.txt")
U2 = data[:,0] #Spannung
E2 = data[:,1] #Feld
U2err = 0.05*U2 #5% Spannungsfehler
E2err = E2/3 #

data = np.loadtxt("plt222.txt")
U3 = data[:,0] #Spannung
E3 = data[:,1] #Feld
U3err = 0.05*U3 #5% Spannungsfehler
E3err = E3/3 #

data = np.loadtxt("plt236.txt")
U4 = data[:,0] #Spannung
E4 = data[:,1] #Feld
U4err = 0.05*U4 #5% Spannungsfehler
E4err = E4/3 #

data = np.loadtxt("plt253.txt")
U5 = data[:,0] #Spannung
E5 = data[:,1] #Feld
U5err = 0.05*U5 #5% Spannungsfehler
E5err = E5/3 #

data = np.loadtxt("plt274.txt")
U6 = data[:,0] #Spannung
E6 = data[:,1] #Feld
U6err = 0.05*U6 #5% Spannungsfehler
E6err = E6/3 #

data = np.loadtxt("plt302.txt")
U7 = data[:,0] #Spannung
E7 = data[:,1] #Feld
U7err = 0.05*U7 #5% Spannungsfehler
E7err = E7/3 #

data = np.loadtxt("plt340.txt")
U8 = data[:,0] #Spannung
E8 = data[:,1] #Feld
U8err = 0.05*U8 #5% Spannungsfehler
E8err = E8/3 #

data = np.loadtxt("plt397.txt")
U9 = data[:,0] #Spannung
E9 = data[:,1] #Feld
U9err = 0.05*U9 #5% Spannungsfehler
E9err = E9/3 #

data = np.loadtxt("plt500.txt")
U10 = data[:,0] #Spannung
E10 = data[:,1] #Feld
U10err = 0.05*U10 #5% Spannungsfehler
E10err = E10/3 #
'''
'''
plt.title('$E$ gegen $U_{B}$ fuer verschiedene $r$')
plt.errorbar(U1,E1,xerr = U1err,yerr=E1err,fmt="bo",label="r=200mm")  #1
plt.errorbar(U2,E2,xerr = U2err,yerr=E2err,fmt="go",label="r=210mm") #2
plt.errorbar(U3,E3,xerr = U3err,yerr=E3err,fmt="co",label="r=222mm") #3
plt.errorbar(U4,E4,xerr = U4err,yerr=E4err,fmt="mo",label="r=236mm") #4
plt.errorbar(U5,E5,xerr = U5err,yerr=E5err,fmt="ro",label="r=253mm") #5
plt.errorbar(U6,E6,xerr = U6err,yerr=E6err,fmt="ko",label="r=274mm") #6
plt.errorbar(U7,E7,xerr = U7err,yerr=E7err,fmt="bo",label="r=302mm") #7
plt.errorbar(U8,E8,xerr = U8err,yerr=E8err,fmt="go",label="r=340mm") #8
plt.errorbar(U9,E9,xerr = U9err,yerr=E9err,fmt="co",label="r=397mm") #9
plt.errorbar(U10,E10,xerr = U10err,yerr=E10err,fmt="mo",label="r=500mm") #10
'''
plt.xlabel(r'$U$ [V]')
plt.ylabel(r'$E$ [$\frac{kV}{m}$]')

def f(x,a,b): #Fitfunktion, x-Achsen-Wert immer zuerst!
    return a*x+b

params1, pcov1 = opt.curve_fit(f, U1, E1) #1
perr1 = np.sqrt(np.diag(pcov1))
print ('Anstieg1:\t', params1[0], '+/- ',perr1[0])
print ('Achsenabschnitt1:\t', params1[1], '+/-', perr1[1])

params2, pcov2 = opt.curve_fit(f, U2, E2) #2
perr2 = np.sqrt(np.diag(pcov2))
print ('Anstieg2:\t', params2[0], '+/- ',perr2[0])
print ('Achsenabschnitt2:\t', params2[1], '+/-', perr2[1])

params3, pcov3 = opt.curve_fit(f, U3, E3) #3
perr3 = np.sqrt(np.diag(pcov3))
print ('Anstieg3:\t', params3[0], '+/- ',perr3[0])
print ('Achsenabschnitt3:\t', params3[1], '+/-', perr3[1])

params4, pcov4 = opt.curve_fit(f, U4, E4) #4
perr4 = np.sqrt(np.diag(pcov4))
print ('Anstieg4:\t', params4[0], '+/- ',perr4[0])
print ('Achsenabschnitt4:\t', params4[1], '+/-', perr4[1])

params5, pcov5 = opt.curve_fit(f, U5, E5) #5
perr5 = np.sqrt(np.diag(pcov5))
print ('Anstieg5:\t', params5[0], '+/- ',perr5[0])
print ('Achsenabschnitt5:\t', params5[1], '+/-', perr5[1])

params6, pcov6 = opt.curve_fit(f, U6, E6) #6
perr6 = np.sqrt(np.diag(pcov6))
print ('Anstieg6:\t', params6[0], '+/- ',perr6[0])
print ('Achsenabschnitt6:\t', params6[1], '+/-', perr6[1])

params7, pcov7 = opt.curve_fit(f, U7, E7) #7
perr7 = np.sqrt(np.diag(pcov7))
print ('Anstieg7:\t', params7[0], '+/- ',perr7[0])
print ('Achsenabschnitt7:\t', params7[1], '+/-', perr7[1])

params8, pcov8 = opt.curve_fit(f, U8, E8) #8
perr8 = np.sqrt(np.diag(pcov8))
print ('Anstieg8:\t', params8[0], '+/- ',perr8[0])
print ('Achsenabschnitt8:\t', params8[1], '+/-', perr8[1])

params9, pcov9 = opt.curve_fit(f, U9, E9) #9
perr9 = np.sqrt(np.diag(pcov9))
print ('Anstieg9:\t', params9[0], '+/- ',perr9[0])
print ('Achsenabschnitt9:\t', params9[1], '+/-', perr9[1])

params10, pcov10 = opt.curve_fit(f, U10, E10) #10
perr10 = np.sqrt(np.diag(pcov10))
print ('Anstieg10:\t', params10[0], '+/- ',perr10[0])
print ('Achsenabschnitt10:\t', params10[1], '+/-', perr10[1])

x_axis = np.linspace(0,U1[-1],num=100)
plt.plot(x_axis, f(x_axis,params1[0],params1[1]), markersize=0.05, label=r'Fit1: (Parameter)', color='b') #1
plt.plot(x_axis, f(x_axis,params2[0],params2[1]), markersize=0.05, label=r'Fit2: (Parameter)', color='g') #2
plt.plot(x_axis, f(x_axis,params3[0],params3[1]), markersize=0.05, label=r'Fit3: (Parameter)', color='c') #3
plt.plot(x_axis, f(x_axis,params4[0],params4[1]), markersize=0.05, label=r'Fit4: (Parameter)', color='m') #4
plt.plot(x_axis, f(x_axis,params5[0],params5[1]), markersize=0.05, label=r'Fit5: (Parameter)', color='r') #5
plt.plot(x_axis, f(x_axis,params6[0],params6[1]), markersize=0.05, label=r'Fit6: (Parameter)', color='k') #6
plt.plot(x_axis, f(x_axis,params7[0],params7[1]), markersize=0.05, label=r'Fit7: (Parameter)', color='b') #7
plt.plot(x_axis, f(x_axis,params8[0],params8[1]), markersize=0.05, label=r'Fit8: (Parameter)', color='g') #8
plt.plot(x_axis, f(x_axis,params9[0],params9[1]), markersize=0.05, label=r'Fit9: (Parameter)', color='c') #9
plt.plot(x_axis, f(x_axis,params10[0],params10[1]), markersize=0.05, label=r'Fit10: (Parameter)', color='m') #10
#plt.legend(loc='upper left')

# Shrink current axis by 20%
box = plt.get_position()
plt.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

fig = plt.gcf()
plt.show()
fig.savefig('ausw1_1.eps')
