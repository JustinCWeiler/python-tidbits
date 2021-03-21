# Euler's method for dy/dt=f(t,y)
# Here, f(t,y) = t+y, y(0)=1, \Delta t = 0.5, 0<=t<=5

# Import packages needed
import numpy as np
import matplotlib.pyplot as plt

# Create f(t,y) for dy/dt = t+y
def dydt(t,y):
    return t+y

# Create empty list for our y values that we'll find
y = []

# Add initial value of y to list (here, y(0)=1)
y.append(1)

# Step size
dt = 0.5

# Interval used for t
interval = [0,5]

# Number of iterations/steps in calc
iterNum = (interval[1]-interval[0])/dt

# Create grid for t
t = np.linspace(interval[0],interval[1],iterNum + 1)

# Find number of iterations needed
iter = len(t)-1

# Create Euler's Method function
def eulersMethod(k):
    for i in range(0,k):
        y.append(y[i] + dydt(t[i],y[i])*dt)
    return y

y = eulersMethod(iter)

# If you want to print out your results, uncomment these lines
print("The values of t are", t)
print("The values of y are", y)



# Plot function
plt.plot(t, y)

# Plot labels
# label axes
plt.xlabel('t')
plt.ylabel('y')

# title
plt.title("Euler's Method for dy/dt = t+y\n (created by Dr. Hohn)")

# show plot
plt.show()
