import numpy as np
from numpy import cos, sin, exp

z = 0 + 1j
# define the imagineary number

# CONSTANTS
e = 1.602 * 10 ** -19
# fundamental charge in C
eps_0 = 8.85 * 10 ** -12
# permittivity of the vacuum in C^2 N^-1 m^-2
m = 9.11 * 10 ** -31
# mass of electron in kg
h_bar = 6.58 * 10 ** -16
# reduced plank constant in eVs
c = 3*10**8

# for sodium
n = 2.54 * 10 ** 28
# number density of electrons in m^-3

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
# complex refractive index

theta = 0
cos_theta = np.cos(theta)
# at the end we should integrate through all angles, for the moment focus on incident.

p = N*cos_theta

k_0 = w/c

d = 200
# depth of layer in nm

M = np.matrix( [cos(k_0 * N * d * cos_theta)   (-z/p)*sin(k_0 * N * d * cos_theta) ], [-zp*sin(k_0 * N * d * cos_theta) , cos(k_0 * N * z * cos_theta)] )
