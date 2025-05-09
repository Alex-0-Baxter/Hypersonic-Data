import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Constants
acc_gravity = 9.81  # meters/seconds^2
density_air = 1.225
karman_line = 100000  # meters

# Read data
data1 = pd.read_csv('REPO/CONE_DATA.csv') 
data2 = pd.read_csv('REPO/MANHOLE_DATA.csv')  
data3 = pd.read_csv('REPO/SPHERE_DATA.csv')  

x1 = data1['time'].values
y1 = data1['position'].values

x2 = data2['time'].values
y2 = data2['position'].values

x3 = data3['time'].values
y3 = data3['position'].values

# Numerical differentiation to calculate velocity (dy/dx)
dy1_dx = np.gradient(y1, x1)
dy2_dx = np.gradient(y2, x2)
dy3_dx = np.gradient(y3, x3)

fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, sharex=False, sharey=True)


ax1.plot(x1, dy1_dx)
ax2.plot(x2, dy2_dx)
ax3.plot(x3, dy3_dx)

ax1.set_title('Cone Velocity')
ax2.set_title('Manhole Velocity')
ax3.set_title('Sphere Velocity')


for ax in (ax1, ax2, ax3):
    ax.grid(True)
    

fig.text(0.5, 0.04, 'Time (Seconds)', ha='center')
fig.text(0.04, 0.5, 'Velocity (Meters/Second)', va='center', rotation='vertical')
fig.text(0.5, 0.96, 'Simulation Velocity Data', ha='center',fontsize=16)

plt.tight_layout()
plt.show()
