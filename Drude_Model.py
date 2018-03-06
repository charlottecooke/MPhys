from numpy import cos, inf, zeros, array, exp, conj, nan, isnan, pi, sin

import numpy as np
import cmath
import time

# for sodium
n = 2.54 * 10 ** 28
# number density of electrons in m^-3

e = 1.602 * 10 ** -19
# fundamental charge in C

eps_0 = 8.85 * 10 ** -12
# permittivity of the vacuum in C^2 N^-1 m^-2

m = 9.11 * 10 ** -31
# mass of electron in kg

h_bar = 6.58 * 10 ** -16
# reduced plank constant in eVs

steps = int(10/0.1) + 1
w = np.empty((steps))
filler = np.arange(0,10.1,0.1)
index_w = np.arange(w.size)
np.put(w,index_w,filler)

w = w + 0j
# make w complex

plas_w = np.sqrt((n*e**2)/(eps_0*m))
# plasmon frequency in units of s^-1

plas_w_eV = plas_w * h_bar

N = np.sqrt( 1 - (plas_w_eV**2/w**2))

# for w in range(len(w)):
#     if w > plas_w_eV:
#         N = np.sqrt( 1 - (plas_w_eV**2/w**2))
#     else:
#         N= 0
# complex refractive index (from Textbook)

R = np.absolute((1-N)/(1+N)) **2
# relfection coefficient

import matplotlib.pyplot as plt

# plot a graph of time against current
plt.plot(w,R)
plt.xlabel('Photon Energy (eV)')
plt.ylabel('Reflection')
plt.grid(True)
