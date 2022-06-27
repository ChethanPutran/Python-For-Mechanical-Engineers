#######################################################################################
#from sympy import symbols, solve
import math


# x = symbols('x')


#(For Loop)
#Initial condition
# x = 0

# for iter in range(100):
#     x_new = math.sqrt((5* x - 3)/2)
   
#     if abs(x_new - x) < 0.000001:
#         break
#     x = x_new
# print("The root : %0.5f" % x_new)    
# print("The no. of iterations : %d" % iter)

#Initial condition
x = 2
x_new = 0
while abs(x_new - x) < 0.000001:
    x_new = math.sqrt((5 * x - 3) / 2)
    
print("The root : %0.5f" % x_new)    
  