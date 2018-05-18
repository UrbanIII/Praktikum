import numpy as np
import matplotlib.pyplot as plt

a = np.loadtxt("data")
print(a)
plt.plot(a[:,0],a[:,1])
plt.show()
