import pyaudio
import audioop
import numpy as np
import time
import matplotlib.pyplot as plt
import pylab
import pygame
import scipy as cp


RATE = 44100
#CHUNK = int(RATE/20)
CHUNK = 2**10

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=2,rate=RATE,input=True,
              frames_per_buffer=CHUNK)
t1=0
t2=0

volume=0

loud=[]

L2=0
VU=""

while(1):
#for i in range (100):
    if(t1==0):
        t1=time.time()
    data = np.frombuffer(stream.read(CHUNK),dtype=np.int16).astype(np.float)
    peak=np.max(data)
    rms=np.sqrt( np.mean(data**2) )
    loud.append(rms)
    L1 = 20*np.log10(peak)
    widmo=np.fft.rfft(data)
    #widmo=np.abs(widmo)
    #poziom="="*int(50*peak/2**16)
    PK="="*int(L1/5)   
    #print(data)
    
    '''pylab.semilogx(widmo)
    pylab.grid()
    pylab.savefig("03.png",dpi=100)
    pylab.close('all')
    
    plt.axhline(L1)
    pylab.grid()
    pylab.axis([0,5,0,90])
    pylab.savefig("04.png",dpi=100)
    pylab.close('all')
    
    plt.axhline(L2)
    pylab.grid()
    pylab.axis([0,5,0,90])
    pylab.savefig("05.png",dpi=100)
    pylab.close('all')'''
    
    t2=time.time()
    if(t2-t1>0.3):
        volume=np.sqrt( np.mean(np.average(loud)**2) )
        L2 = 20*np.log10(volume)
        VU="-"*int(L2/5)
        t1=0
        loud.clear()

    print(np.min(data),"\t",np.max(data),"\t",np.average(np.abs(data)))

stream.stop_stream()
stream.close()
p.terminate()