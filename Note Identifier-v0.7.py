import matplotlib.pyplot as plt
from scipy.fftpack import fft
from Rhythmus import Rhythmus
from scipy.io import wavfile
import numpy as np
from pylab import*
import datetime
import pyaudio
import wave
import math


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
#name = "Accoustic 32 notes 2.wav"
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

def maximo(array):
    mid = int(len(array)/2)
    maximo = 0
    for i in range(mid):
        if abs(array[i]) > abs(array[maximo]):
            maximo = i
    return maximo





def media(array):
    soma = 0
    for i in range(len(array/2)):
        if array[i] > 1:
            soma = soma + abs(array[i])
    soma = soma/len(array/2)
    return soma





def note(y):
    note = round(math.log(math.pow(y/440, 12), 2))

    note = note + mode

    if note >= 0:
        while note > 12:
            note = note - 12
            #print(note)
    else:
        while note < -12:
            note = note + 12
            #print(note)
    
    if note == 0 or note == 12 or note == -12:
        return "A"
    if note == 1 or note == -1:
        return "A#"
    if note == 2 or note == -2:
        return "B"
    if note == 3 or note == -3:
        return "C"
    if note == 4 or note == -4:
        return "C#"
    if note == 5 or note == -5:
        return "D"
    if note == 6 or note == -6:
        return "D#"
    if note == 7 or note == -7:
        return "E"
    if note == 8 or note == -8:
        return "F"
    if note == 9 or note == -9:
        return "F#"
    if note == 10 or note == -10:
        return "G"
    if note == 11 or note == -11:
        return "G#"





def freq(x):
    return 440 * math.pow(2, x/12)




################################################################################################
#           1 - Basic
def Basic(info):    
    sampFreq, snd = wavfile.read(info['name'])

    snd = snd / (2.**15)

    info['points'] = snd.shape[0]

    if len(snd.shape) == 1:
        s1 = snd[:]
    else:
        s1 = snd[:, 0]

    info['s1'] = s1
    info['fa'] = info['points']/music_length

    return info
 
################################################################################################
#           2 - Separation

def Separation(info):
    end = Rhythmus.go(info)

    info['janelas'] = end['janelas']
    info['tempo'] = end['tempo']
    info['tempos'] = end['tempos']
    
    total = 0
    x = 0

    s2 = []

    p = info['s1'][ total:( total + info['janelas'][0]) ]
    plt.plot(p, color='k')
    plt.show()

    while total < info['points']:
        a = []
        a.append( info['s1'][ total:( total + info['janelas'][x]) ] )
        s2.append(a[0])
        total = total + info['janelas'][x]
        x = x + 1

    info['s2'] = s2
    return info

################################################################################################
#           3 - FFT
def FFT(info):
    notas = []
    f_notes = []

    for i in range(len(info['s2'])):
        yf = abs(fft(info['s2'][i]))
        fft_ = maximo(yf)

        Tjanela = info['janelas'][i]/info['fa']
        
        f_notes.append(round(fft_*( 1/Tjanela )))
        notas.append(note(f_notes[-1]))

    info['notas'] = notas
    info['f_notes'] = f_notes
    return info
################################################################################################
#           4 - Prints

def PRINT(info):
    print('')
    print('f_notes')
    print(info['f_notes'])
    print('')
    print('notas')
    print(info['notas'])
    print('')
    print('end[\'tempos\']')
    print(info['tempos'])
    print('')
    plt.plot(info['s1'], color='k')

    plt.show()
    input()

def Analyze(mode, name, music_length):
    info = {}
    info['mode'] = mode
    info['name'] = name
    info['music_length'] = music_length

    PRINT( FFT( Separation( Basic(info) ) ) )

if __name__ == '__main__':
    print("Modos:\n")
    print("Cello\t?")
    print("Piano\t8")
    print("\nModo:")
    mode = int(input())

    print('\nNome:')
    name = str(input())

    print('\nTempo total (em segundos):')
    music_length = int(input())

    Analyze(mode, name, music_length)

