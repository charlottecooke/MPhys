from numpy import cos, inf, zeros, array, exp, conj, nan, isnan, pi, sin

import numpy as np
import scipy as sp
import time

start_time = time.time()

cos_theta0 = 1
# at first set theta1 to 0
cos_theta1 = 1
# when theta1 is 0, then so too is theta1
cos_theta2 = 1
# when theta1 is 0, then so too is theta2
n_0 = 1
# for air the refractive index is ~1

# refractive index of ITO glass
n_2 = 1.902

# code below can be used to choose between a substrate of Copper or Glass
# material = str(input("Is the substrate Copper or Glass? "))
#
# if material == "Copper":
#     n_2 = 0.637
# elif material == "Glass":
#     n_2 = 1.902
# else:
#     print("invalid input")
#     exit()
# choose between Cu or ITO glass refractive indecies
print(n_2)

# we want n to vary between 0 and 3 with a step of 0.1
steps = int(3/0.1) + 1
n = np.empty((steps))
filler = np.arange(0,3.1,0.1)
index_n = np.arange(n.size)
np.put(n,index_n,filler)

# we want k to vary between 0 and 3 with a step of 0.1
k = np.empty((steps))
index_k = np.arange(k.size)
np.put(k,index_k,filler)

n = np.array(n)
k = np.array(k).reshape((-1, 1))
n_com = n + k.repeat(len(n), 1) * 1j

print (n_com)
print ( "time", time.time() - start_time)

r_01 = (cos_theta0 - n_com*cos_theta1)/(cos_theta0 + n_com*cos_theta1)
t_01 = (2*cos_theta0)/(cos_theta0 + n_com*cos_theta1)

# print(r_01)
# print(t_01)

r_12 = (n_com*cos_theta1 - n_2*cos_theta2)/(n_com*cos_theta1 + n_2*cos_theta2)
t_12 = (2*n_com*cos_theta1)/(n_com*cos_theta1 + n_2*cos_theta2)

# print(r_12)
# print(t_12)

lamda = 500 # in units nm
d = 200  # in units nm
beta = ((2*np.pi)/lamda)*n_com*d*cos_theta1

# print("Beta is equal to {}".format(beta))

z = 0 + 1j

block = np.exp(2*z*beta)
# double check whether this is e^+ or e^- 

# not sure if this is defo doing what we hope
# but it is cycling through the set because we do have
# values at each "step"

# n is what we are changing

# should I be running over both i and j?

for i in r_01, r_12, block:
    for j in i:
        r_film = (r_01 + (r_12*block))/(1 + r_01*r_12*block)
    # print r_film

print ( "time 2", time.time() - start_time)
# find r_film for all value of n contained in the array

for i in t_01, t_12, block:
    for j in i:
        t_film = (t_01*t_12*block)/(1 + r_01*r_12*block)

# find the absolute value of this and then square it
ABS_R = np.absolute(r_film)
# print(ABS_R)
R = np.power(ABS_R,2)
# find the value of R which is equal to square of absolute value of r

ABS_T = np.absolute(t_film)
# print(ABS_T)
T = n_2*np.power(ABS_T,2)
# find the value of T which is equal to square of absolute value of t

A = 1 - T - R

print ( "time 3", time.time() - start_time)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(n,k,T, rstride=2, cstride=2)
ax.set_ylabel('k')
ax.set_xlabel('n')
ax.set_title('Transmisson')

plt.savefig('/Users/luka/Documents/University/MPhys/Theory/n&k_plot_T.jpg')

plt.clf()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(n,k,R, rstride=2, cstride=2)
ax.set_ylabel('k')
ax.set_xlabel('n')
ax.set_title('Reflection') 

plt.savefig('/Users/luka/Documents/University/MPhys/Theory/n&k_plot_R.jpg')

plt.clf()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(n,k,A, rstride=2, cstride=2)
ax.set_ylabel('k')
ax.set_xlabel('n')
ax.set_title('Absorption')

plt.savefig('/Users/luka/Documents/University/MPhys/Theory/n&k_plot_A.jpg')
