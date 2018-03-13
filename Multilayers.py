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

# so for now just layers of the same thing
# gonna do sodium so that I know it works
n = 2.98 * 10 ** 28

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

#gonna keep p1 because I think we will need to do something with this later
p1 = N*cos_theta


k_0 = w/c

d = 200
# depth of layer in nm

#as long as the matrices have the same dimensions we can multiply them without need to edit them
# that makes this a lot simpler!
M1 = np.append([[cos(k_0*N*d*cos_theta), (-z/p1)*sin(k_0 * N * d * cos_theta)]], [[-z*p1*sin(k_0 * N * d * cos_theta), cos(k_0 * N * z * cos_theta)]], axis=0)

#and we could just multiply the characteristic equation by essentially itself 
#but with different values 
# and then that two tone if you like matrix can be used to form the larger one
# in either of the two ways given in the book
# I definitely think the work is not done on the other code though
M = M1 ** 30

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