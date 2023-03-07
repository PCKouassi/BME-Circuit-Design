import numpy as np
import matplotlib.pyplot as plt
w= 1
A= 1
t= np.arange(-2, 3*np.pi, 0.01) #time scale
h= [5, 10, 20, 100] #values for orders
plot_data = []
Summation = []
# Plotting the harmonics
# 5th Harmonic
for n in range(1, 5):
    # Defining Terms of equation
    term1 = ((-4 * A) / (np.pi**2 * n**2)) * np.cos(n * w * t)
    term2 = ((2 * A) / (np.pi * n)) * np.sin(n * w * t)
    term3 = (1 - np.cos(np.pi * n))
    Summation.append(((term1 + term2)*term3))
    plot_data = Summation[n-1]
    plt.plot(t, plot_data, 'b-')
    plt.title('{}''th Harmonic'.format(h[0]))
    plt.xlabel('Time (s)')
    plt.ylabel('f(t)')
plt.show()

# 10th Harmonic
for n in range(1, 10):
    # Defining Terms of equation
    term1 = ((-4 * A) / (np.pi**2 * n**2)) * np.cos(n * w * t)
    term2 = ((2 * A) / (np.pi * n)) * np.sin(n * w * t)
    term3 = (1 - np.cos(np.pi * n))
    Summation.append(((term1 + term2)*term3))
    plot_data = Summation[n-1]
    plt.plot(t, plot_data, 'b-')
    plt.title('{}''th Harmonic'.format(h[1]))
    plt.xlabel('Time (s)')
    plt.ylabel('f(t)')
plt.show()

# 20th harmonic
for n in range(1, 20):
    # Defining Terms of equation
    term1 = ((-4 * A) / (np.pi**2 * n**2)) * np.cos(n * w * t)
    term2 = ((2 * A) / (np.pi * n)) * np.sin(n * w * t)
    term3 = (1 - np.cos(np.pi * n))
    Summation.append(((term1 + term2)*term3))
    plot_data = Summation[n-1]
    plt.plot(t, plot_data, 'b-')
    plt.title('{}''th Harmonic'.format(h[2]))
    plt.xlabel('Time (s)')
    plt.ylabel('f(t)')
plt.show()

# 100th harmonic
for n in range(1, 100):
    # Defining Terms of equation
    term1 = ((-4 * A) / (np.pi**2 * n**2)) * np.cos(n * w * t)
    term2 = ((2 * A) / (np.pi * n)) * np.sin(n * w * t)
    term3 = (1 - np.cos(np.pi * n))
    Summation.append(((term1 + term2)*term3))
    plot_data = Summation[n-1]
    plt.plot(t, plot_data, 'b-')
    plt.title('{}''th Harmonic'.format(h[3]))
    plt.xlabel('Time (s)')
    plt.ylabel('f(t)')
plt.show()

# Plotting the Periodical Function Reconstruction
# 5th Harmonic
Summation=[]
for n in range(1, 5):
    # Defining Terms of equation
    term1 = ((-4 * A) / (np.pi**2 * n**2)) * np.cos(n * w * t)
    term2 = ((2 * A) / (np.pi * n)) * np.sin(n * w * t)
    term3 = (1 - np.cos(np.pi * n))
    Summation.append(((term1 + term2)*term3))
    plot_data = sum(Summation)
plt.plot(t, plot_data, 'b-')
plt.title('{}''th Harmonic Periodical Function Reconstruction'.format(h[0]))
plt.xlabel('Time (s)')
plt.ylabel('f(t)')
plt.show()

# 10th Harmonic
Summation = []
for n in range(1, 10):
    # Defining Terms of equation
    term1 = ((-4 * A) / (np.pi**2 * n**2)) * np.cos(n * w * t)
    term2 = ((2 * A) / (np.pi * n)) * np.sin(n * w * t)
    term3 = (1 - np.cos(np.pi * n))
    Summation.append(((term1 + term2)*term3))
    plot_data = sum(Summation)
plt.plot(t, plot_data, 'b-')
plt.title('{}''th Harmonic Periodical Function Reconstruction'.format(h[1]))
plt.xlabel('Time (s)')
plt.ylabel('f(t)')
plt.show()

# 20th Harmonic
Summation = []
for n in range(1, 20):
    # Defining Terms of equation
    term1 = ((-4 * A) / (np.pi**2 * n**2)) * np.cos(n * w * t)
    term2 = ((2 * A) / (np.pi * n)) * np.sin(n * w * t)
    term3 = (1 - np.cos(np.pi * n))
    Summation.append(((term1 + term2)*term3))
    plot_data = sum(Summation)
plt.plot(t, plot_data, 'b-')
plt.title('{}''th Harmonic Periodical Function Reconstruction'.format(h[3]))
plt.xlabel('Time (s)')
plt.ylabel('f(t)')
plt.show()

# 100th Harmonic
Summation = []
for n in range(1, 100):
    # Defining Terms of equation
    term1 = ((-4 * A) / (np.pi**2 * n**2)) * np.cos(n * w * t)
    term2 = ((2 * A) / (np.pi * n)) * np.sin(n * w * t)
    term3 = (1 - np.cos(np.pi * n))
    Summation.append(((term1 + term2)*term3))
    plot_data = sum(Summation)
plt.plot(t, plot_data, 'b-')
plt.title('{}''th Harmonic Periodical Function Reconstruction'.format(h[3]))
plt.xlabel('Time (s)')
plt.ylabel('f(t)')
plt.show()
