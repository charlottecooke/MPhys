import pandas as pd
import numpy as np
import time

start_time = time.time()

df2 = pd.read_excel('http://rredc.nrel.gov/solar/spectra/am1.5/ASTMG173/ASTMG173.xls')

print ( 'time 1', time.time() - start_time)

Wavelength_nm = df2.iloc[1:,0]
# Wavelegnth in nm, ignores the first entry which is the title

Flux_per_Wavelength = df2.iloc[1:,2]
# SFD in units of W/m^2nm (remember to ignore the first entry which is the title, using [1:,2])

SFD = Flux_per_Wavelength * 10**9
# SFD in units of W/m^3

WaveL_nm = np.array(Wavelength_nm)
# WaveL in units of m expressed as a numpy array

WaveL = WaveL_nm * 10**-9
# WaveL in units of m

l = len(WaveL_nm) + 1

Flux = np.array(SFD)
# This is the Flux in units of W/m^3 expressed as a numpy array
## check that the units of this are right from MatLab code

print ( 'time 2', time.time() - start_time)

import matplotlib.pyplot as plt

plt.plot(Wavelength_nm, SFD)
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (W/m^3)')
# plt.show()

import scipy.constants
import scipy

e = scipy.constants.e
h = scipy.constants.h
c = scipy.constants.c

# we want the sum to run until WaveL is 1010nm, above this the photons are not
# energetic enough to split H2O
k_temp = np.where(WaveL_nm==1010)
k = int(k_temp[0])

I = []

# because we discard any energy above band gap E = 1.24eV we only want Flux at WaveL = 1010nm
for i in range(1,k):
    I_temp = (e * Flux[i] * WaveL[i])/(h*c) * (WaveL[i+1]-WaveL[i])
    I.append(I_temp)

I_max = sum(I)*10**-1
# max theoretical current in units of mA/cm^2 disregarding electrons below 1.24eV

print('Maximum theoretical current is', I_max, 'mA/cm^2')

I_T = []
I_T_temp = []

for i in range(1,l-2):
    I_T_temp = (e * Flux[i] * WaveL[i])/(h*c) * (WaveL[i+1]-WaveL[i])
    I_T.append(I_T_temp)

I_T_max = sum(I_T)*10**-1
# max total current, without taking bandgap into account, in units of mA/cm^2

print(I_T_max)

efficiency = I_max/I_T_max
# are we dicounting the excess energy of photons that are above the 1.24eV band gap
# in the right way?

print(efficiency)

print ( 'time 3', time.time() - start_time)

# now find maximum number of photons

N_electrons = (Flux * WaveL)/(h*c)

Max_N_electrons = max(N_electrons)

index_temp = np.where(N_electrons == Max_N_electrons)
Max_N_index = int(index_temp[0])

Max_N_WaveL_nm = WaveL_nm[Max_N_index]

print('The maximum number of photons occur at', Max_N_WaveL_nm, 'nm')

# find the most energetic point of spetcrum in terms of wavelength
Max_Flux = max(Flux)

flux_index_temp = np.where(Flux == Max_Flux)
Max_Flux_Index = int(flux_index_temp[0])

Max_Flux_WaveL_nm = WaveL_nm[Max_Flux_Index]

print('The most energetic point of the spectrum is at', Max_Flux_WaveL_nm, 'nm')
