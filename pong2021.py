import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

plt.ion()
winSize = 200
fig = plt.figure()
ax = fig.add_subplot(111)
t = np.arange(winSize)
volt = np.zeros(len(t))
tbar = [winSize-5,winSize-5,winSize-5]
vbar = [.25,.5,.75]
ballx = winSize/4
bally = 2.5
dx = winSize/2/100
dyy = np.random.rand(1)-0.5
dy = dyy[0]/50
balldir = 1
line1,line2, line3 = ax.plot(t, volt, 'k:',tbar,vbar,'b*',ballx,bally,'ro') 
plt.axis([0,winSize,-1,6])

try:
    import nscopeapi as nsapi
    ns = nsapi.nScope()
except Exception as e:
    print("Unable to communicate with nScope")
    print(e)
else:
    print("Successfully opened connection to nScope!")

ns.setChannelsOn(True,False,False,False)
ns.setSampleRateInHz(100)
ns.requestData(3000)
tstart = time.time()
f = 0
score = 0
scoretime = tstart

while ns.requestHasData():
    d = ns.readData(1)
    volt=np.roll(volt,-1)
    volt[-1] = d
    
    ballx = ballx + balldir*dx;
    bally = bally + dy;
    
    if (ballx > winSize):
        ballx = winSize/4
        bally = 2.5
        balldir = 1
        dx = winSize/2/100
        dyy = np.random.rand(1)-0.5
        dy = dyy[0]/50
        score = score - 10
        
    if((ballx > winSize-25)and(ballx < winSize)and(bally > d-.35)and(bally < d + .35)):
        if time.time() > scoretime + 1:
            score = score + 5
            print(score)
            scoretime = time.time()
            balldir = balldir * -1
            '''if paddle > prevpaddle
                dy = paddle - prevpaddle;
                if dy > 2
                    dy = 2;
                end
                if dy < -2
                    dy = -2;
             '''
    
    if ((ballx < 10)and(balldir == -1)):
        balldir = balldir * -1
    
    if bally > 4.5:
        dy = dy * -1

    if bally < 0.5:
        dy = dy * -1

    
    f=f+1
    if(f==10):
        #print(1/(time.time()-tstart))
        tstart = time.time()
        
        #rect = patches.Rectangle((10,10),25,25,linewidth=1,edgecolor='r',facecolor='none')
        #ax.add_patch(rect)
        
        line1.set_ydata(volt)
        line2.set_data(tbar,[volt[-1]-.25,volt[-1],volt[-1]+.25])
        line3.set_data(ballx,bally)
        fig.canvas.draw()
        fig.canvas.flush_events()
        f=0
        
print("Done! Score = ")
print(score)

