import time
import matplotlib.pyplot as plt
import numpy as np 


try:
    import nscopeapi as nsapi
    ns = nsapi.nScope()
except Exception as e:
    print("Unable to communicate with nScope")
    print(e)
else:
    print("Successfully opened connection to nscope!")

ns.setChannelsOn(True, False, False, False)
ns.setSampleRateInHz(100)  # Sample Rate
ns.requestData(1500)
data = []
ts = []
peaklist= [2.5]
peaktimes= [time.time()]
toter = []
while ns.requestHasData():
    # nscope data aquisition 
    d = ns.readData(1)
    data.append(d)
    t = time.time()
    ts.append(t)
    # algorithm
    if (len(data) >= 3): # Minimum number of data points required
        if ((data[-2]-data[-1] > 0) and (data[-3]-data[-2] < 0) and (data[-2] > 4)): # Slope and Minimmum magnitude Conditions
            if (ts[-2] - peaktimes[-1] > .4): # Time condition
                peaktimes.append(ts[-2])  # Peak times 
                peaklist.append(data[-2]) # Corresponding peak data points
                BPM = (1/(peaktimes[-1]-peaktimes[-2]))*60 # BPM Calculation 
                toter.append(BPM)
                print('Calculated BPM= ', round(BPM)) # BPM output

rate= np.mean(toter)
 
if rate >=90:
    print('Take a chhill pill dude, relax a bit!')
elif rate <= 45:
        print('You gotta get more active, do some jumping jacks!')
elif rate <=90 and rate >= 45:
    print('I see that youre taking it easy! Have a chill day!')
