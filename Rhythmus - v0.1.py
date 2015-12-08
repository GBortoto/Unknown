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
    
    def graph(name):
        #name = 'All.wav'
        sampFreq, snd = wavfile.read(name)

        snd = snd / (2.**15)
        #print("snd.shape: "+ str(snd.shape))

        points = snd.shape[0]
        #print(points)

        if len(snd.shape) == 1:
            s1 = snd[:]
        else:
            s1 = snd[:, 0]
            #print(snd.shape[0])
        return s1

    def bpm(s1):
        s3 = s1

        for i in range(len(s3)):
            if s3[i] < 0:
                s3[i] = 0

        sorted_s1 = sort(s3)

        for i in range(len(s1)):
            if s3[i] < sorted_s1[len(s1) - len(s1)/10 ]:
                s3[i] = 0
            else:
                s3[i] = 1

        #plt.plot(s3, color='k')
        #plt.show()

        ######     #####     #####     ### ##     ####    ###
        ######     #####     #####     ### ##     ####    ###
        ######     #####     #####     ### ##     ####    ###
        ######     #####     #####     ### ##     ####    ###
        ######     #####     #####     ### ##     ####    ###
        ######     #####     #####     ### ##     ####    ###
        ######     #####     #####     ### ##     ####    ###
        ######     #####     #####     ### ##     ####    ###
        ######     #####     #####     ### ##     ####    ###
        ######     #####     #####     ### ##     ####    ###
        ######     #####     #####     ### ##     ####    ###
        ######     #####     #####     ### ##     ####    ###
        ######     #####     #####     ### ##     ####    ###
        ######     #####     #####     ### ##     ####    ###

        white_size = 0
        white_erro = 0
        white_space = []

        black_space_inicio = []
        black_space_final = []

        n = 5000
        
        for i in range(len(s3)):
            if s3[i] == 1:
                if  white_erro > n:
                    black_space_inicio.append(i)
                    #black_space_final.append(i-black_space_inicio[])
                if white_size > 0:
                    white_space.append(white_size)
                    white_size = 0
                white_erro = 0
            
            if s3[i] == 0:
                # if len(spaces) > 0:
                if white_erro == n:
                    black_space_final.append(i-n)
                if white_erro > n:
                    
                    white_erro = white_erro + 1
                    white_size = white_erro
                else:
                    white_erro = white_erro + 1
              #  else:
                  #  pass

        plt.plot(s3, color='k')
        plt.show()
        
        black_space = []

        for i in range(len(white_space)+1):
            if i == 0:
                black_space.append(black_space_final[0])
            else:
                black_space.append(black_space_final[i] - black_space_inicio[i-1])
                    
        if white_size > 0:
            white_space.append(white_size)
        white_size = 0
        white_erro = 0

        janelas = []
        for i in range(len(white_space)):
            janelas.append(white_space[i] + black_space[i-1])

        minimo = 1000000000

        for i in range(len(white_space)):
            if (white_space[i] + black_space[i]) < minimo:
                minimo = white_space[i] + black_space[i]

        tempos = []
        for i in range(len(white_space)):
            tempos.append( round((white_space[i] + black_space[i])/minimo) )

            
        end = {}
        end['janelas'] = janelas
        end['tempo'] = minimo
        end['tempos'] = tempos
        end['s1'] = s1

        return end

    def go(name):
        s1 = Rhythmus.graph(name)
        end = Rhythmus.bpm(s1)
        return end
