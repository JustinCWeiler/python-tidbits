# Plot a slope field for dy/dt = f(t,y)
# Our example here is for dy/dt = t + y

# Import packages needed
import numpy as np
import matplotlib.pyplot as plt

# Create f(t,y) for dy/dt = t + y
def dydt(t,y):
    return t+y

# Create grid for ty-plane
t = np.linspace(-10,10,25)
y = np.linspace(-10,10,25)

# Create loop to plot slopes where slope = f(t,y)
for i in t:
    for j in y:
        slope = dydt(i,j)
        # Create domain around each (t,y) point for the slope line
        domain = np.linspace(i-0.05,i+0.05,2)
        # Create funtion to compute lines for slopes
        def linesForSlope(t1,y1):
            z = slope*(domain-t1)+y1
            return z
        # Plot slope lines as computed
        plt.plot(domain,linesForSlope(i,j),solid_capstyle='projecting',solid_joinstyle='bevel')

# Plot graph with all slope lines computed
# Title for plot
plt.title("Slope field for dy/dt = t+y\n (created by Dr. Hohn)")

# Label axes
plt.xlabel('t')
plt.ylabel('y')

# Create a grid on the plot
plt.grid(True)

# Draw plot
plt.show()
