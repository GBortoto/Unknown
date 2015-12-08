from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt
from pylab import*
from scipy.io import wavfile
import math

class Rhythmus():
    staticmethod

    bpm = 0
    s1 = []
    end = {}
        
    def media(array):
        soma = 0
        for i in range(len(array)):
            soma = soma + abs(array[i])
        soma = soma/len(array)
        return soma



    def separador(s1):
        pos_pico = []
        pos_pico_limite = 0
        starts = []
        ends = []
        holdstart = 0
        pico = 0
        
        for i in range(len(s1)):
            if math.fabs(s1[i]) < 0.1:
                if pos_pico_limite != 0:
                    pos_pico_limite = i-1
                    starts.append(holdstart)
                    holdstart = 0
                    ends.append(pos_pico_limite)
                    pos_pico_limite = 0
                pass
            
            if i == 0:
                pass
            
            soma = math.fabs(s1[i]) + math.fabs(s1[i-1])

            if soma >= ( pico-(pico/10) ):
                pico = soma

                if holdstart == 0:
                    print('PICO - COMEÇO')
                    holdstart = i-1
                pass

            if soma < ( pico - (pico/10) ):
                if len(pos_pico) < 5:
                    pos_pico.append(soma)
                    pos_pico_limite = i
                else:
                    #print(pos_pico)
                    if soma <= (Rhythmus.media(pos_pico) + ( Rhythmus.media(pos_pico)/10 )):
                        #print('TESTETESTETESTE')
                        pos_pico.append(soma)
                        pos_pico_limite = i
                    else:
                        #print('PICO - COMEÇO')
                        starts.append(holdstart)
                        holdstart = i
                        ends.append(pos_pico_limite)
                        pos_pico_limite = 0

        end = {}
        end['starts'] = starts
        end['ends'] =  ends
        return end

    
    def RemoveNegativos(s1):
        for i in range(len(s1)):
            if(s1[i] < 0):
                s1[i] = 0
        return s1
        
    def FindPicos(negativos, s1, info):
        picos = []

        count = 0
        n = 1000

        if negativos == False:
            while (info['points'] - count) > 0:
                s2 = s1[count : (count+n) ]
                picos.append(s2.argmax() + count)
                count = count + n
                
        if negativos == True:
            while (info['points'] - count) > 0:
                s2 = s1[count : (count+n) ]
                picos.append(s2.argmax() + count)
                picos.append(s2.argmin() + count)
                count = count + n

        return picos

    def buildGraphic(s1, negativos, info):
        sf = Rhythmus.FindPicos(negativos, s1, info)
        tmp = []
        
        for i in range(len(sf)):
            tmp.append(s1[sf[i]])

        return tmp

    def go(info):
        s1 = info['s1']

        s2 = Rhythmus.buildGraphic(s1, True, info)

        plt.plot(s2)
        plt.show()

        end = Rhythmus.separador(s2)
        
        print(end['starts'])
        print(end['ends'])
        return end
