from sklearn import preprocessing
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

freq=       [1, 10, 25, 50, 100, 150, 200, 250, 500, 750, 1e3, 1.25e3, 1.5e3, 1.75e3, 2e3]
ptpdatach1= [.2, .8, 1.2, 2.4, 3.2, 3.6, 3.6, 3.6, 3, 2.4, 2, 1.6, 1.4, 1.2, 0.8]
ptpdatach2= [0.4, 3, 4, 4, 4.4, 4.4, 4.4, 4.4, 4.4, 4.4, 4.4, 4.4, 4.4, 4.4, 4.4]

ptp_normch1= [x / max(ptpdatach1) for x in ptpdatach1]
ptp_normch2= [x / max(ptpdatach2) for x in ptpdatach2]

# Plotting for Channel 1
plt.plot(freq, ptp_normch1, 'b-')
plt.locator_params(nbins=5, axis='x')  # 5 ticks along x axis
plt.locator_params(nbins=10, axis='y')  # 10 to ticks along y axis
# Add title and axis names
plt.title('Channel 1')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Peak-to-peak Output (V)')
plt.show()

# Plotting for Channel 2
plt.plot(freq, ptp_normch2, 'b-')
plt.locator_params(nbins=5, axis='x')  # 5 ticks along x axis
plt.locator_params(nbins=10, axis='y')  # 10 to ticks along y axis
# Add title and axis names
plt.title('Channel 2')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Peak-to-peak Output (V)')
plt.show()