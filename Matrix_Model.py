# Luka's work modded by me

import numpy as np
from numpy import cos, sin

z = 0 + 1j
# define the imaginary number

# CONSTANTS
e = 1.602 * 10 ** -19
# fundamental charge in C
eps_0 = 8.85 * 10 ** -12
# permittivity of the vacuum in C^2 N^-1 m^-2
m = 9.11 * 10 ** -31
# mass of electron in kg
h_bar = 6.58 * 10 ** -16
# reduced plank constant in eVs
c = 3*10**8

# for sodium
n = 2.54 * 10 ** 28
# number density of electrons in m^-3

#ok here we have the creation of our array of w values
steps = int(10/0.1) + 1
w = np.empty((steps))
filler = np.arange(0,10.1,0.1)
index_w = np.arange(w.size)
np.put(w,index_w,filler)

w = w + 0j
# make w complex
#put in an arbitrary 5.6 for now!!

plas_w = np.sqrt((n*e**2)/(eps_0*m))
# plasmon frequency in units of s^-1

plas_w_eV = plas_w * h_bar


#I think this might be incorrect
N = np.sqrt((1 - (plas_w_eV**2/w**2)))
N[0] = 1
# complex refractive index

theta = 0
cos_theta = np.cos(theta)
# at the end we should integrate through all angles, for the moment focus on incident.

p = N*cos_theta

k_0 = w/c

d = 200
# depth of layer in nm

#trying it with a p l in there
p_l = 1

#as long as the matrices have the same dimensions we can multiply them without need to edit them
# that makes this a lot simpler!
M = np.append([[cos(k_0*N*d*cos_theta), (-z/p)*sin(k_0 * N * d * cos_theta)]], [[-z*p*sin(k_0 * N * d * cos_theta), cos(k_0 * N * z * cos_theta)]], axis=0)

#I think we also said we would be varying the energy of the wave
#calculate r
#remembering we count from 0
length = M.shape[2]

for i in range(length):
    r = ((M.item((0,0,i)) + (M.item((0,1,i))))*p - (M.item((1,0,i)) + (M.item((1,1,i)))))/((M.item((0,0,i)) + (M.item((0,1,i))))*p + (M.item((1,0,i)) + (M.item((1,1,i)))))
    #to get reflectance we square this
    R = (abs(r))**2
    #to get transmission
    t = (2*p)/((M.item((0,0,i)) + M.item((0,1,i)))*p + (M.item((1,0,i)) + M.item((1,1,i))))
    #the real value
    T = (1/p)*(abs(t))**2
    A = 1 - T - R
import matplotlib.pyplot as plt

F = N*k_0*d

# plot a graph of time against current
plt.plot(w,T)
plt.xlabel('Photon Energy (eV)')
plt.ylabel('Transmission')
plt.grid(True)
