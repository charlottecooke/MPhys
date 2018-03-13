#Multilayers
# so we still need all of this

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

# so these will change
#is this really how we want to do it?
#magnesium
n1 = 7.95 * 10 ** 28
#boron, not sure about this one
n2 = 2.59 * 10 ** 28
# number density of electrons in m^-3

#ok here we have the creation of our array of w values
steps = int(20/0.1) + 1
w = np.empty((steps))
filler = np.arange(0,20.1,0.1)
index_w = np.arange(w.size)
np.put(w,index_w,filler)

w = w + 0j
# make w complex
#put in an arbitrary 5.6 for now!!

plas_w1 = np.sqrt((n1*e**2)/(eps_0*m))
# plasmon frequency in units of s^-1

plas_w1_eV = plas_w1 * h_bar

plas_w2 = np.sqrt((n2*e**2)/(eps_0*m))
plas_w2_eV = plas_w2 * h_bar

#I think this might be incorrect
N1 = np.sqrt((1 - (plas_w1_eV**2/w**2)))
N1[0] = 1
# complex refractive index
N2 = np.sqrt((1 - (plas_w2_eV**2/w**2)))
N2[0] = 1


theta = 0
cos_theta = np.cos(theta)
# at the end we should integrate through all angles, for the moment focus on incident.

p1 = N1*cos_theta
p2 = N2*cos_theta

k_0 = w/c

d = 100
# depth of layer in nm

#as long as the matrices have the same dimensions we can multiply them without need to edit them
# that makes this a lot simpler!
M1 = np.append([[cos(k_0*N1*d*cos_theta), (-z/p1)*sin(k_0 * N1 * d * cos_theta)]], [[-z*p1*sin(k_0 * N1 * d * cos_theta), cos(k_0 * N1 * z * cos_theta)]], axis=0)
M2 = np.append([[cos(k_0*N2*d*cos_theta), (-z/p2)*sin(k_0 * N2 * d * cos_theta)]], [[-z*p2*sin(k_0 * N2 * d * cos_theta), cos(k_0 * N2 * z * cos_theta)]], axis=0)

#and we could just multiply the characteristic equation by essentially itself 
#but with different values 
# and then that two tone if you like matrix can be used to form the larger one
# in either of the two ways given in the book
# I definitely think the work is not done on the other code though
Y = M1 * M2
M = Y
 
#trying it with a p l in there
p_l = 1


length = M.shape[2]

for i in range(length):
    r = ((M.item((0,0,i)) + (M.item((0,1,i))))*p1 - (M.item((1,0,i)) + (M.item((1,1,i)))))/((M.item((0,0,i)) + (M.item((0,1,i))))*p1 + (M.item((1,0,i)) + (M.item((1,1,i)))))
    #to get reflectance we square this
    R = (abs(r))**2
    #to get transmission
    t = (2*p1)/((M.item((0,0,i)) + M.item((0,1,i)))*p1 + (M.item((1,0,i)) + M.item((1,1,i))))
    #the real value
    T = (1/p1)*(abs(t))**2
    A = 1 - T - R
import matplotlib.pyplot as plt

#F = N1*k_0*d

# plot a graph of time against current
plt.plot(w,R)
plt.xlabel('Photon Energy (eV)')
plt.ylabel('Reflectance')
plt.grid(True)