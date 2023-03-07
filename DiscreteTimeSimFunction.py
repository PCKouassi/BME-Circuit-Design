import matplotlib
import matplotlib.pyplot as plt 
import numpy as np

# Coefficients
rcoeff = np.array([1.0, 0.0, 0.0])
lcoeff = np.array([1.0, 0.5, 0.0])

# Iput arrays 
x0 = np.zeros(10)# Case 1 of 0 changes withdrawls or deposits
x1 = [1.0, 3.4, -2.7, 2.3, 5.2, 6.4, -2.0, -1.0, 0, 0]
x2 = [3.0, 2.0, -3.0, -1.0, 3.0, 2.5, -4.2, 2.2, 0, 0]
x3 = np.add(x1, x2)

# Initial value array for y[n]
y0 = [0, 25]
y1 = [0, 0]
y2 = [0, 0]
y3 = [0, 25]



# Defining function with inputs
def bankbalance(rcoeff, lcoeff, Nsteps, initial, input):
    # Balance Array
    Balance = [] # Initial balance
    currxlist = input #Assigning the x list
    y = initial #Assigning the y list
    # Iterate Nsteps through the for loop
    for n in range(0, 10):
        currx= currxlist[n]
        curry= y[n+1]
        pasty= y[n]
        updated_balance= (lcoeff[1]*curry) + (rcoeff[0]*currx)
        y.append(updated_balance)
        Balance.append(updated_balance)
    return(Balance)

y0 = bankbalance(rcoeff, lcoeff, 10, y0, x0)
y1 = bankbalance(rcoeff, lcoeff, 10, y1, x1)
y2 = bankbalance(rcoeff, lcoeff, 10, y2, x2)
y3 = bankbalance(rcoeff, lcoeff, 10, y3, x3)

total = np.add(np.add(y0, y1), y2)

plt.plot(np.arange(0,10,1), y3, 'b-')
plt.plot(np.arange(0, 10, 1), total, 'ro')
plt.show()