import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

a = np.loadtxt("data")
print(a)
#plt.plot(a[:,0],a[:,1]) #Very simple plot without any error bars
plt.title("Oh boy...")
plt.xlabel("here we go again...")
plt.legend # This is misused and I should really find out how to properly use it...

plt.errorbar(a[:,0],a[:,1],xerr=0.5,yerr=0.5*a[:,1], fmt='go-.', ecolor="r")

x_axis = np.linspace(a[0,0]-1,a[-1,0],num=100)
#print x_axis

# Polynomial fitting with numpy - this yields pretty much the same result as he method below.
#fit = np.polyfit(a[:,0],a[:,1],3,full=True)
#print fit
#fit_func = np.poly1d(fit[0])
#print fit_func
#plt.plot(x_axis,fit_func(x_axis))

# Optimization with scipy
def f(x,a,b,c,d): # IT IS *VERY* IMPORTANT THAT X IS THE FIRST VARIABLE IN THIS LIST. (scipy.opt.curve_fit assumes this form)
    return a*x**3+b*x**2+c*x+d

params, pcov = opt.curve_fit(f, a[:,0], a[:,1])
print params
print pcov
perr = np.sqrt(np.diag(pcov))
print perr
fit_func = np.poly1d(params)
plt.plot(x_axis, fit_func(x_axis))

fig = plt.gcf() #only necessary, because plot destroys the 'current' figure
plt.show() #By default, this destroys the figure (meaning that the command below will produce an empty image)
fig.savefig("Datei.eps") #without the above command, one could simply write plt.savefig("...")
