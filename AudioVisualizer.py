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
    


stream.stop_stream()
stream.close()
p.terminate()