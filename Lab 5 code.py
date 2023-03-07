import matplotlib.pyplot as plt
import csv
import matplotlib
import math

matplotlib.use('TkAgg')
plt.clf()
t = []
data = []
with open('HW5data10.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        t.append(float(row[0]))
        data.append(float(row[1]))

num_data = len(t)  # number of data points = length of list
max_time = max(t)  # length of sample time is the max value in the time list
# sample rate is the number of samples devided by the max time
samp_rate = num_data/max_time
print("The number of data points is {}, the length of the sample time was {}, the sample rate is {}".format(
    num_data, max_time, samp_rate))

t2 = t[0::10]  # select every 10thdata point in t and save it into t2
# select every 10thdata point in data and save it into data2
data2 = data[0::10]

print("The number of data points was {}, and the new number of data points is {}".format(
    num_data, len(data2)))  # test to check the number of data points before and after blurring

# Algorithm
tpeak = [0]  # the list to store the time where a peak occurs
datapeak = []  # a list to store the voltage where a peak occurs
# The list to store the differences in time between the peaks
peak_time_diff = []
location = []
maxes = []
count = 0
for i in range(len(data2)-1):  # for loop that determines peaks
    curr_data = data2[i] #storing testing voltage 
    curr_time = t2[i] # storing testing voltage time
    slope_next = data2[1+i]-curr_data # slope between testing voltage and the next voltage  
    slope_prev = curr_data-data2[i-1] # slope between testing voltage and previous voltage 

    # If the slope between the current voltage and the previous voltage is negative and the slope between the
    # the current voltatge and the next is positive, then the current voltage is a peak
    if slope_prev < 0 and slope_next > 0:  # absolute peak conditoin
        if curr_data < 0.70*min(data2):  # minimum peak voltage condition
            count = count+1  # counter for peak appending
            tpeak.append(t2[i])  # store the coresponding peak time in tpeak
            time_sep = tpeak[count]-tpeak[count-1]
            if time_sep > 0.1:  # period condition
                # store the peak voltage into datapeak
                datapeak.append(data2[i])
                location.append(i)  # store location of peak in list
    elif slope_prev == 0 or slope_next == 0:  # flat "peaks"
        if curr_data < 0.70*min(data2):  # minimum peak voltage condition
            count = count+1  # counter for peak appending
            tpeak.append(t2[i])  # store the coresponding peak time in tpeak
            time_sep = tpeak[count]-tpeak[count-1]
            if time_sep > 0.1:  # period condition
                # store the peak voltage into datapeak
                datapeak.append(data2[i])
                location.append(i)  # store location of peak in list

BPM = (len(datapeak) / (max(t2)-min(t2)))*60

print("Calculated BPM= {}".format(BPM))
markers_on = location
plt.plot(t2, data2, 'b-', markevery=markers_on,
         marker='*', ms=20, mec='r', mfc='r') # markers for stars on peaks
plt.locator_params(nbins=5, axis='x')  # 5 ticks along x axis
plt.locator_params(nbins=10, axis='y')  # 10 to ticks along y axis
# Add title and axis names
plt.title('BPM= {}'.format(round(BPM)))
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.show()
