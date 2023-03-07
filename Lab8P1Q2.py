import matplotlib.pyplot as plt
import numpy as np
import time

# Opening Nscope
try:
    import nscopeapi as nsapi
    ns = nsapi.nScope()
except Exception as e:
    print("Unable to communicate with nScope")
    print(e)
else:
    print("Successfully opened connection to nscope!")

# Setting Data Recording Settings
ns.setChannelsOn(True, False, False, False) #turns on recording for channel 1 and 2
ns.setSampleRateInHz(2000)  # Sample Rate
ns.requestData(4000)
data1 = []
data2 = []

# Frequency Value
dt = 1/8000
# Time list
t = np.arange(0, 0.5, dt)
print("Data collection started!")
# Data Request
while ns.requestHasData():
    d = ns.readData(1)
    data1.append(d)
print("Data Collected!")

Fs= len(t)/t[-1] # Calculates sample rate
Ts = 1.0/Fs # sampling interval
y = data1# from the csv file
n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq= k/T # two sides frequency range
frq = frq[range(int(n/2))] # one side frequency range
Y = np.fft.fft(y)/n # fft computing and normalization
Y = Y[range(int(n/2))]
# Plot Section
fig, ax = plt.subplots(3, 1)
fig.suptitle("Channel 1")
ax[0].plot(t,y)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Voltage (V)')
ax[1].plot(frq,abs(Y),'r') # plotting the spectrum
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')
ax[2].loglog(frq,abs(Y),'r') # plotting the spectrum
ax[2].set_xlabel('Freq (Hz)')
ax[2].set_ylabel('|Y(freq)|')
plt.show()


