import matplotlib.pyplot as plt
import numpy as np

try:
    import nscopeapi as nsapi 
    ns = nsapi.nScope()
except Exception as e:
        print("Unable to communicate with nScope")
        print (e)
else:
    print("Successfully opened connection to nscope!")

ns.setChannelsOn(True, False, False, False)
ns.setSampleRateInHz(4000) # Sample Rate 
ns.requestData(1000) 
data = []
print("Data collection started!")
while ns.requestHasData():
    d = ns.readData(1)
    data.append(d)
print("Data Collected!")

dt= 1/2000
t= np.arange(0, 0.5, dt)

plt.plot(t,data,'k-')
plt.title('ECG Output')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.show()

x = data 
NFFT = 1024 #length of the windowing segments 
Fs= int(1.0/dt) # Sampling Freq.
fig, (ax1, ax2)= plt.subplots(nrows=2, constrained_layout=True) # Making one figure for subplots

ax1.plot(t,x) #first plot 
# Labeling plot components
ax1.title.set_text('ECG Output') 
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Voltage (V)')
Pxx, freqs, bins, im = ax2.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=900) # Plotting Spectrogram to help chose filter 
# Labeling plot components
ax2.title.set_text('ECG Output Spectrogram')
ax2.set_xlabel('Time(s)')
ax2.set_ylabel('Frequency(Hz)')
plt.show()

