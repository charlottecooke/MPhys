# lets try that again but better

#Multilayers by with Chebyshev polynomials
# so we still need all of this
#I'm gonna label all of these how they do in the book for simplicity

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
n1 = nl = 1
#magnesium
n2 = 7.95 * 10 ** 28
#boron, not sure about this one
n3 = 2.59 * 10 ** 28
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

plas_w2 = np.sqrt((n2*e**2)/(eps_0*m))
# plasmon frequency in units of s^-1

plas_w2_eV = plas_w2 * h_bar

plas_w3 = np.sqrt((n3*e**2)/(eps_0*m))
plas_w3_eV = plas_w3 * h_bar

#I think this might be incorrect
N2 = np.sqrt((1 - (plas_w2_eV**2/w**2)))
N2[0] = 1
# complex refractive index
N3 = np.sqrt((1 - (plas_w3_eV**2/w**2)))
N3[0] = 1

theta = 0
cos_theta = np.cos(theta)
# at the end we should integrate through all angles, for the moment focus on incident.

p1 = 1
p2 = N2*cos_theta
p3 = N3*cos_theta
pl = 1

#constant?!
k_0 = w/c

d1 = 100
d2 = 100
# depth of layer in nm

#evaluating beta for the two materials
beta2 = k_0*N2*d1*cos_theta
beta3 = k_0*N3*d2*cos_theta

#how many layers 
N = 100

#what is a?
a = cos(beta2)*cos(beta3) - (1/2)*((p2)/(p3) + (p3)/(p2))*sin(beta2)*sin(beta3)

#these weird coefficients
#this should really be a function but I haven't done that for simplicity and clarity 
UNminus1 = (sin((N)*cos(a)**-1))/(np.sqrt(1 - (a**2)))  
UNminus2 = (sin((N-1)*cos(a)**-1))/(np.sqrt(1 - (a**2)))

#so using the books calc
M = np.append([[((cos(beta2)*cos(beta3) - (p3/p2)*sin(beta2)*sin(beta3))*UNminus1 - UNminus2) , (-z*((1/p3)*cos(beta2)*sin(beta3) + (1/p2)*sin(beta2)*cos(beta3))*UNminus1)]], [[(-z*(p2*sin(beta2)*cos(beta3) + p3*cos(beta2)*sin(beta3))*UNminus1), ((cos(beta2)*cos(beta3) - ((p2)/(p3))*sin(beta2)*sin(beta3))*UNminus1 - UNminus2)]], axis=0)
#fixing nands
# =============================================================================
# M[0,0,0] = 1
# M[0,1,0] = 1
# M[1,0,0] = 1
# M[1,1,0] = 1
# =============================================================================

#size
length = M.shape[2]

r_mat = []

#not currently getting into this loop
for i in range(0, length):
    r = ((M.item((0,0,i)) + (M.item((0,1,i)))*pl)*p1 - (M.item((1,0,i)) + (M.item((1,1,i)))*pl))/((M.item((0,0,i)) + (M.item((0,1,i)))*pl)*p1 + (M.item((1,0,i)) + (M.item((1,1,i)))*pl))
    #r_mat.append(r)
    #to get reflectance we square this
    R = (abs(r))**2
    #to get transmission
    t = (2*p1)/((M.item((0,0,i)) + M.item((0,1,i))*pl)*p1 + (M.item((1,0,i)) + M.item((1,1,i))*pl))
    #the real value
    T = (pl/p1)*(abs(t))**2
    A = 1 - T - R
import matplotlib.pyplot as plt
#F = N1*k_0*d

# plot a graph of time against current
plt.plot(w,R)
plt.xlabel('Photon Energy (eV)')
plt.ylabel('Reflectance')
plt.grid(True)