import numpy as np
import pandas as pd

file_path = "/Users/luka/Downloads/Oct1717x001.dat"

# create a dataframe using pandas of the .dat file
df = pd.read_table(file_path)
print(df)

# extract date from file_path to create name for the file
Name = file_path[22:-4]

# create two series with the information from the dataframe
Time = df.iloc[:,0]
Current_A = df.iloc[:,1]

# convert from Amps to mAmps
Current = Current_A*1000

import matplotlib.pyplot as plt

# plot a graph of time against current 
plt.plot(Time,Current)
plt.xlabel('Time (mins)')
plt.ylabel('Current mA')
plt.grid(True)

# 'get current figure' and save it to figure
fig1 = plt.gcf()

# save the figure to the specified place, using the name from the file_path
fig1.savefig("/Users/luka/Documents/University/MPhys/Data_Analysis/Graph" + Name)
