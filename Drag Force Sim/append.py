########  Python program to calculate drag force against a cyclist #########
import math  #importing math module for mathematical calculations
import matplotlib.pyplot as plt # for plotting graph


#DRAG COEFFICIENT 
drag_coefficient = 1.1

# FrontalArea  (in sq.meters)
area = 4.9

#Density of the fluid(in kg/qubic m)
density = 1.226

#The flow velocity relative tonthe object(in km/h)

velocities = [20,22,24,25,26,27,29,30,35]
 
#Drag Forces for different values of velocity(in N)
forces = []

#For loop to compute each force corresponding to given velocity

for velocity in velocities :#In each iteration each value of velocity is iterated
	force = (0.5*drag_coefficient*area*density*pow(velocity,2))   #Formula for computation of drag force
	forces.append(force)    #appends each computed value of force to the 'forces' list

for force in forces :
	print(f'{force} {"N"}') #prints the different force values
   