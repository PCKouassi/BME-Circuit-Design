import matplotlib.pyplot as plt
import numpy as np

# Calling the NScope
try:
    import nscopeapi as nsapi 
    ns = nsapi.nScope()
except Exception as e:
        print("Unable to communicate with nScope")
        print (e)
else:
    print("Successfully opened connection to nscope!")

# Setting Channels and sample rate settigngs 
ns.setChannelsOn(True, False, False, False)
ns.setSampleRateInHz(4000) # Sample Rate 
ns.requestData(8000) # data points total
data = []
print("Data collection started!")

# Data Collection implimentation  
while ns.requestHasData():
    d = ns.readData(1)
    data.append(d)
print("Data Collected!")

# Plot Features Settings
dt = .00025 # 4kHz sample rate 
t = np.arange(0.0, 2, dt) # Time array for 4kHz sample with 8000 total data points for 2 seconds
x = data
NFFT = 1024  # the length of the windowing segments
Fs = int(1.0 / dt)  # the sampling frequency

fig, (ax1, ax2) = plt.subplots(nrows=2) # Setting the figure for the subplots

# EMG Signal Plotting
ax1.plot(t, x)
ax1.title.set_text('EMG Signal at 4kHz')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Volatage (V)')

# EMG Spectrogram Plotting 
Pxx, freqs, bins, im = ax2.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=900)
ax2.title.set_text('Spectrogram EMG Signal at 4kHz')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Frequency (Hz)')

plt.show()

