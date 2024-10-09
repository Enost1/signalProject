# Question3
# Used fft_example as the basis so some things don't get used but i think will be used in later questions
import numpy as np
from scipy.fft import fft
import math
import matplotlib.pyplot as plt

def cart2pol(x, y):
    # Converts cartesian coordinates to polar coordinates
    theta = np.arctan2(y, x)
    rho = np.sqrt(x**2 + y**2)
    return [theta, rho]

# Add 50 Hz power line interference 
def powerline_interference(signal, fs, f_interference=50, amplitude=0.15):
    t = np.arange(len(signal)) / fs 
    interference = amplitude * np.sin(2 * np.pi * f_interference * t)
    return signal + interference # Return modified signal

def main():
    # Load f.npy
    f_signal = np.load('f.npy').flatten()
    
    fs = 1024  # Sampling frequency
    T = 1 / fs  # Sampling period
    N = len(f_signal)  # N samples
    t = np.arange(N) * T  
    
    # a) 50Hz power line interference 
    corrupted_signal = powerline_interference(f_signal, fs, amplitude=0.15)
    
    # Plot
    plt.figure()
    plt.plot(t, f_signal, label="Original Signal", color='blue', linewidth=0.75)
    plt.plot(t, corrupted_signal, label="Corrupted Signal", color='red', linestyle='dashed', linewidth=0.75)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude [a.u.]')
    plt.legend()
    plt.xlim(t[0], t[-1])
    plt.grid(True)
    plt.show()


   
if __name__ == '__main__':
    main()
