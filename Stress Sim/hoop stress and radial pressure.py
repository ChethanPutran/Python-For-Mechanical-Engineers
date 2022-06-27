  
from mpl_toolkits import mplot3d
import numpy as np 
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D



hoop_stresses = []

radial_pressures = []

x_values=[]
y_values = []
z_values=[]
r1 = 200
r2 = 300
fluid_pressure = 8



# r1 = input('Enter internal radius of the cylinder (in mm): ')
# r1=int(r1)
# print()
# r2 = input("Enter external radius of the cylinder (in mm): ")
# r2=int(r2)
# print()
# fluid_pressure = input("Enter the fluid pressure (in N/sq.mm): ")
# fluid_pressure=int(fluid_pressure)
# print()

b = fluid_pressure*float(pow(r1,2)*pow(r2,2))/float(pow(r2,2)-pow(r1,2))
a = b /float(pow(r1,2)) - fluid_pressure
X=[]
Y = []



radius=np.linspace(r1,r2,50)
angles=np.linspace(0,2*math.pi,50)

for r in radius:
    for i in angles:
        X.append(r * math.cos(i))
        Y.append(r*math.sin(i))
Z = np.linspace(0, 5, len(X))

Xc,Zc = np.meshgrid(X,Z)
radius = np.linspace(r1, r2, len(X))

hoop_stress = (b / radius**2) + a
radial_pressure=(b / radius**2) - a

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(X, Y, Z, c=hoop_stresses, lw=0, s=20)
# new = ax.plot_surface(Xc, Yc, Zc, rstride=1, cstride=1, cmap='jet', edgecolor='black')
ax.set_title("Hoop Stress Across Thickness")
ax.set_xlabel("Radius(in mm)")
ax.set_ylabel("Hoop Stess(N/sq.mm)")
plt.style.use('classic')
plt.show()



