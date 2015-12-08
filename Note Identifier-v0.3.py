import pyaudio
import wave
import datetime
"""
y = []

#Information about the "stream" object
###################################
CHUNK = 1024       # bytes
RATE = 44100       # Hz
CHANNELS = 2       # Mono or Stereo
RECORD_SECONDS = 5 # Seconds
###################################

#Information about the "output.wave" file
FORMAT = pyaudio.paInt16
"""

name = "Accoustic 32 notes 2.wav"
""" 
WAVE_OUTPUT_FILENAME = name

p = pyaudio.PyAudio()

# Creating the object stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

# Creating the array that stores all the data
frames = []

# Recording process (???)
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)    

print("* done recording")

# Closings (???)
stream.stop_stream()
stream.close()
p.terminate()

            # Creating the "output.wave"

# Setting up the file configurations
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)

# Transporting the data from the array "frames" to the file
wf.writeframes(b''.join(frames))

# Closing the file ("saving")
wf.close()
"""
########################################################################################################################

from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt
from pylab import*
from scipy.io import wavfile
import math

if __name__ == '__main__':
    print("starting")

def maximo(yf):
    mid = int(len(yf)/2)
    maximo = 0
    for i in range(mid):
        if abs(yf[i]) > abs(yf[maximo]):
            maximo = i
    return maximo

def note(y):
    note = round(math.log(math.pow(y/440, 12), 2))
#    print("NOTE")
#    print(note)
    
    if note > 0:
        while note > 6:
            note = note-8

    else:
        while note < -6:
            note = note+8
        
    if note == 0:
        return "A"
    if note == 1 or note == -1:
        return "B"
    if note == 2 or note == -2:
        return "C"
    if note == 3 or note == -3:
        return "D"
    if note == 4 or note == -4:
        return "E"
    if note == 5 or note == -5:
        return "F"
    if note == 6 or note == -6:
        return "G"
#    else:
#        print(note)
        
def freq(x):
    return 440 * math.pow(2, x/12)

n_notes = int(input())

sampFreq, snd = wavfile.read(name)

snd = snd / (2.**15)
#print("snd.shape: "+ str(snd.shape))

points = snd.shape[0]
#print(snd.shape)

if len(snd.shape) == 1:
    s1 = snd[:]
else:
    s1 = snd[:, 0]
    #print(snd.shape[0])
#print("s1")
#print(s1)

s2 = []

count = 1
amostragem = points/n_notes
#print(amostragem)
total = 0

while n_notes+1 > count:
    a = []
    #print(amostragem*count)
    a.append(s1[total:(amostragem*count)])
    
    s2.append(a)

    total = total + amostragem
    count = count + 1


#print("s2")
#print(s2)

timeArray = arange(0, points, 1) # <-- Tempo


#timeArray = timeArray / sampFreq
#timeArray = timeArray #scale to milliseconds
#print(timeArray)
#amostragem = 1/len(timeArray)

f_notes = []
for i in range(len(s2)):
    #print(s2[i])
    yf = abs(fft(s2[i]))
#    print("YF")
#    print(yf)
#    print(maximo(yf[0]))
    #print("YF")
    #print(yf)
    #print(yf[0])
    f_notes.append(maximo(yf[0]))
    
#yf = abs(fft(s1))












#x = abs(yf)

plt.plot(s1, color='k')

print(f_notes)
#print("A sua onda tem "+str(maximo(yf))+"Hz")

plot(s1, color='k')
#ylabel('Intensity')
#xlabel('Frequency = '+str(maximo(yf))+"Hz"+"        "+name)

plt.show()
input()
