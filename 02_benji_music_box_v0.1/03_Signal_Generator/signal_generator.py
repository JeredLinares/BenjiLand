'''
Signal Generator

JD Linares
2025 01 23
'''

import pandas as pd
import math


signal_frequency = 261
signal_period = 1 / signal_frequency
signal_amplitude = 32768

sample_frequency = 44100
sample_interval = 1/44100

loop_sample_count = signal_period * sample_frequency

def signal_equation(period,amplitude,time_val):

    return amplitude * math.sin((2*math.pi/period)*time_val) + signal_amplitude



amplitudes = list()

for i in range(169):
    amplitudes.append(int(signal_equation(signal_period,signal_amplitude,i*sample_interval)))

pd.DataFrame(data=amplitudes).to_csv('signal_amplitudes.raw',index=False,header=False)



