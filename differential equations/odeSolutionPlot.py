# Example of using Python's solver for ode
# Simple harmonic oscillator
# dx/dt = y
# dy/dt = -x

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


# Create function for ode solver
def f(Y,t):
    x, y = Y
    dYdt = [x-x*y, -1000*y+y*x]
    return dYdt

# Make values for t for solver
tspan = np.linspace(0, 1, 1001)

# Plot initial condition
initialCondition = [100.0, 10.0]

# Initiate solver
Ysolution = odeint(f,initialCondition, tspan)

# Plot solutions to ODE on top of vector field
plt.plot(tspan, Ysolution[:,0],'b', label = 'x') # path
plt.plot(tspan, Ysolution[:,1],'r', label = 'y') # start
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()

# Show graph
plt.show()
