import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

########GLOBAL_CONSTANTS########
global acc_gravity 
acc_gravity = 9.81 #meters/seconds^2

global density_air
density_air = 1.225

##DRAG COEFFICENIENTS
global drag_flat_plate
global drag_prism
global drag_bullet
global drag_sphere
global drag_airfoil

def DragCoefficent(drag, rho, v, a):
    cd = drag/(rho*(v*v*a/2))
    return cd

##HEIGHT
global karman_line
karman_line = 100000 #meters


data1 = pd.read_csv('REPO/CONE_DATA.csv') 
data2 = pd.read_csv('REPO/MANHOLE_DATA.csv')  
data3 = pd.read_csv('REPO/SPHERE_DATA.csv')  


x1 = data1['time'].values
y1 = data1['position'].values

x2 = data2['time'].values
y2 = data2['position'].values

x3 = data3['time'].values
y3 = data3['position'].values


karman_array1 = np.full((1, len(x1)), karman_line, dtype=int)
karman_array2 = np.full((1, len(x2)), karman_line, dtype=int)
karman_array3 = np.full((1, len(x3)), karman_line, dtype=int)

fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, sharex=False, sharey=True)

# Initial Karman line plot
ax1.plot(x1, karman_array1[0], label="Karman Line")
ax2.plot(x2, karman_array2[0], label="Karman Line")
ax3.plot(x3, karman_array3[0], label="Karman Line")

# Plot data for each case
line1, = ax1.plot(x1, y1)
line2, = ax2.plot(x2, y2)
line3, = ax3.plot(x3, y3)

# Formatting plot
ax1.get_xaxis().get_major_formatter().set_scientific(False)
for ax in (ax1, ax2, ax3):
    ax.grid(True)

ax1.set_title('Cone Height')
ax2.set_title('Manhole Height')
ax3.set_title('Sphere Height')

fig.text(0.5, 0.04, 'Time (Seconds)', ha='center')
fig.text(0.04, 0.5, 'Vertical Position (Meters)', va='center', rotation='vertical')
fig.text(0.5, 0.93, 'Live Simulation Height Data', ha='center',fontsize=16)

# Update function for animation
def update(num, x, y, line):
    line.set_data(x[:num], y[:num])
    return line,

# Animation for each plot
ani1 = animation.FuncAnimation(fig, update, len(x1), interval=60, fargs=[x1, y1, line1], blit=True)
ani2 = animation.FuncAnimation(fig, update, len(x2), interval=60, fargs=[x2, y2, line2], blit=True)
ani3 = animation.FuncAnimation(fig, update, len(x3), interval=60, fargs=[x3, y3, line3], blit=True)


plt.show()
