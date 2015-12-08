from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt
from pylab import*
from scipy.io import wavfile

y = [683, 766, 812, 912, 1024, 1085, 1230]

x = ["A", "B", "C", "D", "E", "F", "G"]
plt.plot(y)

ylabel('Frequency')
xlabel(x[0]+"                 "+
       x[1]+"                 "+
       x[2]+"                 "+
       x[3]+"                 "+
       x[4]+"                 "+
       x[5]+"                 "+
       x[6]+"                 ")

plt.grid()
plt.show()
