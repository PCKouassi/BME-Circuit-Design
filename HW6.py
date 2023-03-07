
import numpy as np
import matplotlib.pyplot as plt
import cmath

w = np.arange(0.01,25000,0.1)

g1 = 1/(1+1/(1j*w*1*0.1e-3))
g2 = 1/(1+1/(1j*w*1*0.2e-3))
g3 = 1/(1+1/(1j*w*1*0.5e-3))
g4 = 1/(1+1/(1j*w*1*1e-3))

plt.xlabel("w") 
plt.ylabel("Gain") 
plt.plot(w,g1)
plt.plot(w,g2)
plt.plot(w,g3)
plt.plot(w,g4)
axes = plt.gca()
plt.show()