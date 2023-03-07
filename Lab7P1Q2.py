import csv
import matplotlib.pyplot as plt
import numpy as np

t= []
data1 = []
data2 =[]

# Enter data file here
with open('Filtered and Unfiltered Data.csv') as f: 
    reader = csv.reader(f)
    for row in reader:
            t.append(float(row[0]))
            data1.append(float(row[1]))
            data2.append(float(row[2]))


# Calaculate values for FFT
Fs= len(t)/t[-1] # Calculates sample rate
Ts = 1.0/Fs # sampling interval
y = data2# from the csv file changing data variables to swith to channel 2
n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq= k/T # two sides frequency range
frq = frq[range(int(n/2))] # one side frequency range
Y = np.fft.fft(y)/n # fft computing and normalization
Y = Y[range(int(n/2))]

# Plot Section
fig, ax = plt.subplots(3, 1)
fig.suptitle("Filtered and Amplified")
ax[0].plot(t,y)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[1].plot(frq,abs(Y),'r') # plotting the spectrum
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')
ax[2].loglog(frq,abs(Y),'r') # plotting the spectrum
ax[2].set_xlabel('Freq (Hz)')
ax[2].set_ylabel('|Y(freq)|')
plt.show()